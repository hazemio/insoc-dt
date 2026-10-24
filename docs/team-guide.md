# Team guide

## Weekly routine

| Day | What happens |
|---|---|
| Sunday | Planning: read the week plan, assign tasks, open issues |
| Midweek | Short sync: blockers and PR reviews |
| Thursday | Open PRs for the week's work so reviewers have time |
| Friday | Review, merge, fill the "Weekly notes" in the week README, update the status table |

Adjust the days to your own schedule. The idea is to keep the same rhythm every week.

## Where things go

| What | Where |
|---|---|
| Python code | `src/insoc/<component>/` |
| Tests | `tests/unit/`, `tests/integration/` |
| Lab topologies and device configs | `lab/topologies/`, `lab/configs/` |
| Suricata and Zeek configs | `lab/sensors/` |
| Reports, slides, screenshots, exports of a week | `weeks/week-XX/deliverables/` |
| Paper summaries | `research/papers/` |
| Dataset notes (not the data) | `research/datasets/` |
| Experiment write-ups | `research/experiments/` |
| Diagrams | `docs/diagrams/` |
| Proposal, feedback, spec | `docs/project/` |

## File naming

- Screenshots: `YYYY-MM-DD_area_description.png`, for example `2026-11-02_dashboard_alerts.png`
- Documents: `weekXX_topic_author.ext`, for example `week06_model-comparison_ahmed.pdf`
- Keep each file under 10 MB.

## Uploading files without the command line

Branch protection blocks direct upload to `develop` and `main`, so use a branch:

1. Open the folder on GitHub (for example `weeks/week-03/deliverables/`).
2. Click **Add file** then **Upload files** and drop your files.
3. Under "Commit changes" choose **Create a new branch**, name it `docs/week-03-evidence`.
4. Title the commit `docs(docs): add week 3 evidence` and click **Propose changes**.
5. Open the pull request into **develop** and ask a teammate to review.

## Uploading with Git

```bash
git checkout develop
git pull
git checkout -b docs/week-03-evidence
git add weeks/week-03/deliverables/
git commit -m "docs(docs): add week 3 evidence"
git push -u origin docs/week-03-evidence
```

Then open a PR into `develop` on GitHub.

## What must not be uploaded

- Passwords, API keys, tokens, `.env` files
- Real user data or captures from real networks
- PCAP files, raw datasets, trained models, VM images (they are too big and ignored by Git).
  Store them on shared storage and put the link in `weeks/week-XX/links.md`.

## Reviewing a PR

- Does it do what the title says, and is the scope small?
- Do tests pass, and are new behaviors tested?
- Are files in the right folder and named correctly?
- For response code: allowlist, expiry, rollback and audit log are respected.
- Resolve every conversation before approving the merge.
