"""Score newsletter drafts against Dean's real issues using Jev (TypeSafe AI).

Usage:
    # Put your key in eval/.env as TYPESAFE_API_KEY=... (git ignores this file)
    python3 scripts/judge.py            # score everything in candidates/
    python3 scripts/judge.py --dry-run  # show what would be sent, no API calls
    python3 scripts/judge.py --runs 3   # repeat each draft 3 times (reference order reshuffled)
    python3 scripts/judge.py --blind    # hide names, company and emails so only style is scored

Folder layout (relative to the eval folder):
    issues/                 all 12 real issues (download with scripts/fetch_issues.py;
                            git ignores this folder). The held-back issues are
                            scored automatically as groups "real_holdout" and "tim".
    candidates/<group>/*.md your drafts to score; the folder name is the group
                            (e.g. skill, baseline, generic)
    results/                JSON results and a summary table are written here
"""
import argparse, json, os, random, re, statistics, sys, time, urllib.request, urllib.error
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ISSUES = ROOT / "issues"
CANDIDATES = ROOT / "candidates"
RESULTS = ROOT / "results"
API_URL = "https://api.typesafe.ai/v1/systemone"
MODEL = "jev-latest"

# Kept out of the reference set and scored as test cases instead.
# Three real Dean issues (the control) plus Tim's guest issue (same newsletter, different writer).
HOLDOUT = {
    "lucky-number-7": "real_holdout",
    "anthropic-loses-money-on-its-best": "real_holdout",
    "the-permission-slip": "real_holdout",
    "the-amazon-let-me-forget-about-ai": "tim",
}


# Swapped out in --blind mode so Jev judges style, not who is named.
# Order matters: longer names first.
BLIND_SWAPS = [
    (r"[\w.]+@bridgeaiconsulting\.com", "[EMAIL]"),
    (r"(?:www\.)?bridgeaiconsulting\.com", "[WEBSITE]"),
    (r"\bBridge AI Consulting\b", "[COMPANY]"),
    (r"\bBridge AI\b", "[COMPANY]"),
    (r"\bDean Mazlish\b", "[AUTHOR]"),
    (r"\bTim Diemer\b", "[AUTHOR]"),
    (r"\bDean\b", "[AUTHOR]"),   # case-sensitive, so "their dean" is left alone
    (r"\bTim\b", "[AUTHOR]"),
    (r"\bCOO\b", "[TITLE]"),
    (r"\bFounder & CEO\b", "[TITLE]"),
]
BLIND = False


def anonymize(text: str) -> str:
    for pattern, swap in BLIND_SWAPS:
        text = re.sub(pattern, swap, text)
    return text


def clean(text: str) -> str:
    """Remove things that would give away the source rather than the style."""
    text = re.sub(r"\[\]\([^)]*\)", "", text)                  # image links
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)       # keep link text, drop URL
    text = re.sub(r"https?://\S+", "", text)                    # bare URLs
    text = re.sub(r"^Date: .*$", "", text, flags=re.M)          # date line
    if BLIND:
        text = anonymize(text)
    return re.sub(r"\n{3,}", "\n\n", text).strip()


def load_issues():
    """Split the real issues into the reference set and held-back test cases."""
    refs, held = [], []
    for path in sorted(ISSUES.glob("*.md")):
        slug = path.stem.split("_", 1)[1]
        if slug in HOLDOUT:
            held.append((HOLDOUT[slug], path))
        else:
            refs.append(clean(path.read_text()))
    if not refs:
        sys.exit("No issues found. Run: python3 scripts/fetch_issues.py issues")
    return refs, held


def api_key():
    """Read the key from the environment, or from eval/.env."""
    if os.environ.get("TYPESAFE_API_KEY"):
        return os.environ["TYPESAFE_API_KEY"]
    env = ROOT / ".env"
    if env.exists():
        for line in env.read_text().splitlines():
            name, _, value = line.partition("=")
            if name.strip().removeprefix("export ").strip() == "TYPESAFE_API_KEY":
                return value.strip().strip("'\"")
    sys.exit("No key found. Add TYPESAFE_API_KEY=... to eval/.env")


def score_levels(what):
    return [f"0: Nothing like the reference issues' {what}",
            f"1: Faint resemblance to the reference issues' {what}",
            f"2: Clearly similar {what}, but noticeable differences",
            f"3: Very close to the reference issues' {what}, only small slips",
            f"4: Indistinguishable from the reference issues' {what}"]


QUESTIONS = {
    "same_author": {
        "type": "noul",
        "instructions": "The candidate_issue was written by the same author as the reference_issues, "
                        "for the same newsletter, judged purely on writing style, voice and structure "
                        "(not on which news topics it covers).",
    },
    "voice": {
        "type": "score",
        "instructions": "How closely the candidate_issue matches the reference_issues' voice: sentence rhythm, "
                        "humor, confidence, opinions, word choice and recurring phrases.",
        "criteria": score_levels("voice"),
    },
    "structure": {
        "type": "score",
        "instructions": "How closely the candidate_issue follows the reference_issues' structure: section order, "
                        "section names, preview list, section lengths and overall length.",
        "criteria": score_levels("structure"),
    },
    "hook": {
        "type": "score",
        "instructions": "How closely the candidate_issue's title and opening paragraphs match the way the "
                        "reference_issues open and hook the reader.",
        "criteria": score_levels("titles and openings"),
    },
    "news_format": {
        "type": "score",
        "instructions": "How closely the candidate_issue's news stories match the reference_issues' news format: "
                        "headline style, factual summary, the 'My take' paragraph and the business angle.",
        "criteria": score_levels("news stories"),
    },
    "closing": {
        "type": "score",
        "instructions": "How closely the candidate_issue's ending matches the reference_issues' endings: "
                        "sign-off lines, forward and contact calls to action, signature and referral box.",
        "criteria": score_levels("endings"),
    },
    "business_value": {
        "type": "score",
        "instructions": "How well the candidate_issue matches the reference_issues' focus on practical, specific "
                        "takeaways for non-technical business owners (concrete examples, numbers, actions).",
        "criteria": score_levels("practical business focus"),
    },
}
SCORE_KEYS = [k for k, q in QUESTIONS.items() if q["type"] == "score"]


def call_jev(api_key, state):
    body = json.dumps({"model": MODEL, "state": state, "questions": QUESTIONS}).encode()
    req = urllib.request.Request(API_URL, data=body, method="POST", headers={
        "Authorization": f"Bearer {api_key}", "Content-Type": "application/json"})
    for attempt in range(4):
        try:
            with urllib.request.urlopen(req, timeout=120) as resp:
                return json.load(resp)
        except urllib.error.HTTPError as e:
            detail = e.read().decode(errors="replace")[:500]
            if e.code in (429, 529) and attempt < 3:
                time.sleep(2 ** attempt * 5); continue
            sys.exit(f"Jev API error {e.code}: {detail}")


def answers_of(resp):
    """Pull the numbers we care about out of a Jev response."""
    a = resp.get("answers", resp)  # tolerate either a wrapped or flat answer object
    row = {"same_author": a["same_author"]["noul"]}
    for k in SCORE_KEYS:
        row[k] = a[k]["score"]
    return row


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--runs", type=int, default=1)
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--only", help="score only this candidates group")
    ap.add_argument("--blind", action="store_true", help="hide names, company and emails")
    args = ap.parse_args()
    global BLIND
    BLIND = args.blind

    refs, held = load_issues()
    cands = held + [(p.parent.name, p) for p in sorted(CANDIDATES.glob("*/*.md"))]
    cands = [(g, p) for g, p in cands if not args.only or g == args.only]
    if not cands:
        sys.exit(f"No drafts found in {CANDIDATES}/<group>/*.md")
    mode = "names hidden" if BLIND else "names shown"
    print(f"{len(refs)} reference issues, {len(cands)} drafts, {args.runs} run(s) each, {mode}")

    if args.dry_run:
        words = sum(len(r.split()) for r in refs)
        print(f"Reference text: ~{words} words (~{int(words * 1.35)} tokens). Jev limit is 32k tokens per question.")
        for g, p in cands:
            print(f"  {g}/{p.name}: {len(clean(p.read_text()).split())} words")
        return

    key = api_key()
    jobs = [(g, p, r) for g, p in cands for r in range(args.runs)]
    random.shuffle(jobs)  # blind ordering
    rows = []
    for i, (group, path, run) in enumerate(jobs, 1):
        shuffled = refs[:]; random.shuffle(shuffled)
        state = {"reference_issues": shuffled, "candidate_issue": clean(path.read_text())}
        resp = call_jev(key, state)
        row = {"group": group, "draft": path.stem, "run": run, **answers_of(resp),
               "input_tokens": resp.get("usage", {}).get("input_tokens")}
        rows.append(row)
        print(f"[{i}/{len(jobs)}] {row['group']}/{row['draft']}: same_author={row['same_author']:.2f}")

    RESULTS.mkdir(exist_ok=True)
    stamp = datetime.now().strftime("%Y%m%d-%H%M%S") + ("-blind" if BLIND else "")
    (RESULTS / f"{stamp}.json").write_text(json.dumps(rows, indent=2))
    summary = f"Mode: {mode}\n\n" + summarize(rows)
    (RESULTS / f"{stamp}-summary.md").write_text(summary)
    print("\n" + summary)
    print(f"Saved to results/{stamp}.json and results/{stamp}-summary.md")


def summarize(rows):
    cols = ["same_author"] + SCORE_KEYS
    def table(key):
        groups = {}
        for r in rows:
            groups.setdefault(key(r), []).append(r)
        lines = ["| " + " | ".join(["name"] + cols + ["avg score"]) + " |",
                 "|" + "---|" * (len(cols) + 2)]
        order = sorted(groups, key=lambda g: -statistics.mean(r["same_author"] for r in groups[g]))
        for g in order:
            rs = groups[g]
            vals = [statistics.mean(r[c] for r in rs) for c in cols]
            avg = statistics.mean(vals[1:])
            lines.append("| " + " | ".join([g] + [f"{vals[0]:.2f}"] + [f"{v:.2f}" for v in vals[1:]] + [f"{avg:.2f}"]) + " |")
        return "\n".join(lines)
    return ("## By group\n\nsame_author is a probability (0-1). Other scores are 0-4.\n\n"
            + table(lambda r: r["group"]) + "\n\n## By draft\n\n"
            + table(lambda r: f"{r['group']}/{r['draft']}") + "\n")


if __name__ == "__main__":
    main()
