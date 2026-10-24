# Contributing

## Branches

```
feature/*  fix/*  docs/*  research/*  chore/*  ci/*   ->  develop  ->  main
                                      hotfix/*  ->  main
```

- `main` is always demo-ready. It only accepts PRs from `develop` or `hotfix/*`.
- `develop` is the integration branch. It accepts PRs from topic branches.
- Nobody pushes directly to `main` or `develop`.

## PR title

`type(scope): summary`, for example `feat(response): add temporary IP block`.

Types: feat, fix, docs, research, test, refactor, perf, ci, chore.

## Review steps

1. Author fills the PR checklist and self-reviews.
2. CI passes: `lint`, `test`, `pr-policy`.
3. Reviewers approve: 1 for `develop`, 2 for `main`.
4. Code owners of the changed folders approve.
5. All conversations resolved, then squash merge.

## Rules

- No secrets, real PCAPs or production configs in the repo.
- Active-response code must respect allowlist, expiry, rollback and audit log.
- Attack tools are for the isolated lab only.

## Uploading project files

Files go through a PR like code. See [docs/team-guide.md](docs/team-guide.md) for the
step-by-step upload guide and the folder map.
