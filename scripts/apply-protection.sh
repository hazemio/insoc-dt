#!/usr/bin/env bash
# Run AFTER: repo pushed, teammates accepted invites, CI ran at least once.
# Usage: OWNER=hazemio REPO=insoc-dt ./scripts/apply-protection.sh
set -euo pipefail
: "${OWNER:?set OWNER}"
REPO="${REPO:-insoc-dt}"
FULL="$OWNER/$REPO"

gh api -X PATCH "repos/$FULL" \
  -F allow_squash_merge=true -F allow_merge_commit=false -F allow_rebase_merge=false \
  -F delete_branch_on_merge=true >/dev/null

gh api -X POST "repos/$FULL/rulesets" --input .github/rulesets/develop.json >/dev/null
gh api -X POST "repos/$FULL/rulesets" --input .github/rulesets/main.json >/dev/null
echo "Protection enabled for $FULL"
