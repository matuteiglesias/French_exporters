#!/usr/bin/env bash
# Synchronize an existing fast clone without LFS hydration or broad history fetches.
set -euo pipefail

die() { printf 'ERROR: %s\n' "$*" >&2; exit 1; }
usage() { printf 'Usage: git_fast_sync.sh [--allow-dirty] [BRANCH_OR_REF]\n' >&2; }
du_bytes() { du -sk "$1" 2>/dev/null | awk '{print $1 * 1024}'; }
lfs_count() { [[ -d .git/lfs/objects ]] && find .git/lfs/objects -type f -printf . | wc -c | tr -d ' ' || printf 0; }

allow_dirty=false
case "${1:-}" in
  --allow-dirty) allow_dirty=true; shift ;;
  -h|--help) usage; exit 0 ;;
esac
(($# <= 1)) || { usage; exit 2; }
ref="${1:-$(git branch --show-current)}"
[[ -n "$ref" ]] || die 'supply a branch or ref when HEAD is detached'
git rev-parse --git-dir >/dev/null 2>&1 || die 'run inside the lightweight clone'
git config --get remote.origin.promisor >/dev/null || die 'refusing: this is not a partial/promisor clone'
git sparse-checkout list >/dev/null || die 'refusing: sparse checkout is not active'
if [[ "$allow_dirty" != true ]] && [[ -n "$(git status --porcelain)" ]]; then
  die 'working tree has changes; commit/stash them or pass --allow-dirty'
fi

start_epoch=$(date +%s)
export GIT_LFS_SKIP_SMUDGE=1
git config lfs.skipsmudge true
git config --local filter.lfs.clean cat
git config --local filter.lfs.smudge cat
git config --local filter.lfs.process ''
git config --local filter.lfs.required false
# Fetch one branch ref with bounded history. No tag or broad ref fetch is used.
if git fetch --depth=20 --no-tags origin "+refs/heads/${ref}:refs/remotes/origin/${ref}"; then
  target="refs/remotes/origin/${ref}"
else
  printf 'INFO: %s is not a branch name; fetching it as an explicit ref.\n' "$ref" >&2
  git fetch --depth=20 --no-tags origin "$ref" || die "could not fetch requested ref: $ref"
  target=FETCH_HEAD
fi

# Deepen only when ancestry cannot be determined at the current shallow boundary.
for deepen in 20 40 80 160; do
  if git merge-base --is-ancestor HEAD "$target" 2>/dev/null; then
    git merge --ff-only "$target"
    break
  fi
  if git merge-base --is-ancestor "$target" HEAD 2>/dev/null; then
    printf 'Already at or ahead of fetched commit; no merge performed.\n'
    break
  fi
  printf 'INFO: merge base unavailable at shallow boundary; deepening requested ref by %s commits.\n' "$deepen" >&2
  git fetch --deepen="$deepen" --no-tags origin "+refs/heads/${ref}:refs/remotes/origin/${ref}" || die "unable to deepen $ref"
done
if ! git merge-base --is-ancestor HEAD "$target" && ! git merge-base --is-ancestor "$target" HEAD; then
  die 'cannot establish a fast-forward after bounded incremental deepening; resolve deliberately'
fi

printf 'fetched_commit=%s\n.git_bytes=%s\nshallow=%s\nlfs_payload_objects=%s\nelapsed_seconds=%s\n' \
  "$(git rev-parse "$target")" "$(du_bytes .git)" "$(git rev-parse --is-shallow-repository)" "$(lfs_count)" "$(( $(date +%s) - start_epoch ))"
