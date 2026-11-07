# Bridge AI Newsletter

A Claude skill that writes the weekly Bridge AI newsletter, plus a test that scores drafts against the real issues.

## What's here

- `bridge-ai-newsletter.skill`: the packaged skill. Load it into Claude and ask: "Write next week's Bridge AI newsletter."
- `bridge-ai-newsletter/`: the skill's source (`SKILL.md` plus reference files for the template, voice, research steps and past issues).
- `bridge-ai-newsletter-analysis.md`: notes on the structure, voice and themes of the 12 published issues.
- `eval/`: a test that uses [Jev](https://typesafe.ai) by TypeSafe AI to score how closely a draft matches the real newsletter, plus a format checker.

## Results so far

Names hidden (`--blind`), averaged over 2 runs. `same_author` is 0 to 1; the average score is 0 to 4 across voice, structure, hook, news format, closing and business focus.

| Drafts | Same author | Avg score | Format checks |
|---|---|---|---|
| Skill v2 (2 drafts) | 0.92-0.93 | 3.51-3.57 | 11/11 |
| Real issues held out from the reference set (3) | 0.91-0.93 | 3.45-3.50 | 9-11/11 |
| Plain Claude, same prompt, no skill (2) | 0.92 | 3.07-3.22 | 7-9/11 |
| Another chat imitating the newsletter (2) | 0.83-0.88 | 2.77-2.83 | |
| Generic AI newsletters (2) | 0.09-0.10 | 0.94-1.04 | |

Every news story in the skill drafts was checked against its source: all were real and correctly dated.

## How the test works

Jev gets 8 real issues as reference and one draft to judge. For each draft it returns:

- `same_author`: probability (0 to 1) that the draft was written by the same author.
- Scores from 0 to 4 for voice, structure, hook, news format, closing and business focus.

Drafts are scored in shuffled order and grouped so the results can be compared:

| Group | What it is | Expected result |
|---|---|---|
| `real_holdout` | 3 real issues kept out of the reference set | Highest. If not, the judge can't be trusted. |
| `tim` | A guest issue by a different writer, same newsletter | Just below the real issues |
| `skill` | Drafts written with the skill | As close to the real issues as possible |
| `baseline` | Plain Claude given the same prompt with no skill | Below the skill |
| `generic` | Generic AI newsletters | Lowest |

Drafts in `eval/candidates/baseline` and `eval/candidates/generic` are AI-written test material, not real issues.

## Running it

```bash
cd eval
python3 scripts/fetch_issues.py issues   # download the real issues (kept out of git)
cp .env.example .env                     # then paste your TypeSafe API key into .env
python3 scripts/judge.py --dry-run       # check what will be sent
python3 scripts/judge.py --runs 3        # score every draft 3 times
python3 scripts/judge.py --blind         # hide names, company and emails first
python3 scripts/check_format.py          # objective format rules (closing, links, length, em dashes...)
```

Use `--blind` to measure style alone. Without it, Jev gives credit just for seeing "Dean" and "Bridge AI": filling in the names on a draft raised its same-author score from 0.80 to 0.91 with no other changes. Blind mode replaces names, the company, titles and emails with placeholders in both the drafts and the reference issues.

Results are saved in `eval/results/`. No dependencies beyond Python 3.
