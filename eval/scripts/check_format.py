"""Check drafts against the newsletter's objective format rules.

Usage: python3 scripts/check_format.py [files...]   (default: every draft in candidates/ plus held-back real issues)
"""
import re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CLOSING = [
    "That's it for this week.",
    "That's who this is for.",
    "not in theory, but in your workflows, with your team, on your timeline, reach out at dean@bridgeaiconsulting.com. That's what we're here for.",
    "Founder & CEO, Bridge AI Consulting",
    "Know a business that could use AI? Refer them to Bridge AI and earn 10% of their first year of payments.",
]
SECTIONS = ["The Deep Dive", "From the Field", "AI News Worth Your Time"]
BANNED = ["game-changer", "game changer", "revolutioniz", "ai landscape", "delve", "unlock the", "unlock value",
          "unlock potential", "supercharge", "harness the", "in conclusion", "here's the thing"]
# Lines from past issues. One familiar phrase is fine; more reads like copying.
STOCK = ["push back on the pile-on", "boring is the correct output", "nothing about your tuesday",
         "i'll tell you honestly", "a well-formatted answer is not a checked answer",
         "likely is not the same as true", "read that again", "here's where i landed",
         "now for the business part", "here is the part that matters", "hold that thought",
         "look at what every one of those has in common", "one rule i'd never skip",
         "two things worth doing this week", "knowing what to point it at"]
EMOJI = re.compile("[\U0001F300-\U0001FAFF☀-➿]")


def issue_text(path):
    text = path.read_text().replace("’", "'")
    return re.split(r"\n-{3,}\s*\n+\**Notes for Dean", text)[0]


def check(path):
    t = issue_text(path)
    words = len(re.sub(r"\]\([^)]*\)", "]", t).split())
    stories = len(re.findall(r"\*\*My take:\*\*", t))
    links = len(re.findall(r"\[READ THE [A-Z0-9 .&'-]+ [A-Z]+ →\]", t))
    checks = {
        "1,400-1,900 words": 1400 <= words <= 1900,
        "3 sections": all(s in t for s in SECTIONS),
        "This week: preview": "This week:" in t,
        "no em dashes": "—" not in t,
        "no emojis": not EMOJI.search(t),
        "no banned words": not any(b in t.lower() for b in BANNED),
        "bold My take x3+": stories >= 3,
        "READ THE ... → links x3+": links >= 3,
        "exact closing": all(c in t for c in CLOSING),
        "Why this travels": "this travels:" in t,
        "max 1 reused stock line": sum(x in t.lower() for x in STOCK) <= 1,
    }
    return words, checks


def main():
    paths = [Path(p) for p in sys.argv[1:]] or (
        sorted(ROOT.glob("candidates/*/*.md")) +
        [p for p in sorted((ROOT / "issues").glob("*.md"))
         if any(k in p.name for k in ("lucky-number-7", "anthropic-loses", "permission-slip"))])
    for p in paths:
        words, checks = check(p)
        fails = [k for k, ok in checks.items() if not ok]
        status = "PASS" if not fails else f"{len(checks) - len(fails)}/{len(checks)}"
        print(f"{status:>6}  {p.parent.name}/{p.name} ({words} words)" + (f"  missing: {', '.join(fails)}" if fails else ""))


if __name__ == "__main__":
    main()
