# Branch protection and review policy

```
topic branch --(1 approval + code owners)--> develop --(2 approvals + code owners)--> main
```

| Gate | develop | main |
|---|---|---|
| Pull request required, no force push, no delete | yes | yes |
| Checks `lint`, `test`, `pr-policy` pass, branch up to date | yes | yes |
| Approvals | 1 | 2 |
| Code owner approval | yes | yes |
| Last push approved by someone else | no | yes |
| New commits dismiss old approvals | yes | yes |
| Conversations resolved | yes | yes |
| Squash merge only, linear history | yes | yes |
| Allowed source branch | feature, fix, docs, research, chore, refactor, test, ci, perf | develop, hotfix |

Approvals only count from people with write access who are not the PR author, so invite at
least two collaborators before enabling the rulesets (`scripts/apply-protection.sh`).
The rulesets have no bypass list: the owner follows the same rules.

Optional hardening: add `{"type": "required_signatures"}` to `.github/rulesets/main.json`
once everyone signs commits.
