#!/usr/bin/env bash
# Provision a shallow, sparse, blobless Git clone without automatic LFS hydration.
set -euo pipefail

readonly DEFAULT_REPO_URL='https://github.com/matuteiglesias/French_exporters.git'
readonly SPARSE_PATHS=(
  '/AGENTS.md'
  '/research/'
  '/scripts/'
  '/docs/'
  '/notebooks/02_Statistical_Analysis_and_Modeling/Thesis/'
  '/notebooks/06_Visualization_and_Presentation/'
  '/Notes/'
)

die() { printf 'ERROR: %s\n' "$*" >&2; exit 1; }
usage() { cat <<'USAGE'
Usage: git_fast_clone.sh [--repo-url URL] DESTINATION [BRANCH_OR_REF]

Creates a new shallow, partial, sparse clone. Repository URL defaults to
$FAST_GIT_REPO_URL or the French_exporters GitHub repository.
USAGE
}
du_bytes() { du -sk "$1" 2>/dev/null | awk '{print $1 * 1024}'; }
lfs_metrics() {
  local lfs_dir="$1/.git/lfs/objects" count=0 bytes=0
  if [[ -d "$lfs_dir" ]]; then
    count=$(find "$lfs_dir" -type f -printf '.' | wc -c | tr -d ' ')
    bytes=$(du_bytes "$lfs_dir")
  fi
  printf '%s %s\n' "$count" "$bytes"
}

repo_url="${FAST_GIT_REPO_URL:-$DEFAULT_REPO_URL}"
while (($#)); do
  case "$1" in
    --repo-url) (($# >= 2)) || die '--repo-url requires a URL'; repo_url="$2"; shift 2 ;;
    -h|--help) usage; exit 0 ;;
    --*) die "unknown option: $1" ;;
    *) break ;;
  esac
done
(($# >= 1 && $# <= 2)) || { usage >&2; exit 2; }
dest="$1"
requested_ref="${2:-}"
[[ ! -e "$dest" ]] || die "destination already exists: $dest"

start_epoch=$(date +%s)
export GIT_LFS_SKIP_SMUDGE=1
printf 'Cloning %s into %s with blob filtering, depth 1, and sparse checkout.\n' "$repo_url" "$dest"
git clone --filter=blob:none --depth=1 --sparse --no-tags --no-checkout "$repo_url" "$dest"
cd "$dest"
# Override global LFS filters locally with pass-through filters.  This keeps LFS
# pointers as pointers and avoids a global LFS installation hydrating them during checkout.
git config lfs.skipsmudge true
git config --local filter.lfs.clean cat
git config --local filter.lfs.smudge cat
git config --local filter.lfs.process ''
git config --local filter.lfs.required false
git config --local remote.origin.tagOpt --no-tags
git sparse-checkout set --no-cone "${SPARSE_PATHS[@]}"

if [[ -n "$requested_ref" ]]; then
  # A heads refspec avoids broad ref discovery and keeps only the requested branch.
  if git fetch --depth=1 --no-tags origin "+refs/heads/${requested_ref}:refs/remotes/origin/${requested_ref}"; then
    git checkout --detach "refs/remotes/origin/${requested_ref}"
  else
    printf 'INFO: %s is not a branch name; trying it as an explicit ref.\n' "$requested_ref" >&2
    git fetch --depth=1 --no-tags origin "$requested_ref" || die "could not fetch requested ref: $requested_ref"
    git checkout --detach FETCH_HEAD
  fi
else
  git checkout --detach origin/HEAD
fi

git config --get remote.origin.promisor >/dev/null || die 'partial-clone promisor configuration is not active'
git config --get remote.origin.partialclonefilter | grep -qx 'blob:none' || die 'blob:none filter is not active'
git sparse-checkout list >/dev/null || die 'sparse checkout is not active'
git rev-parse --is-shallow-repository | grep -qx true || die 'clone is not shallow'
read -r lfs_count lfs_bytes < <(lfs_metrics "$PWD")
elapsed=$(( $(date +%s) - start_epoch ))
printf 'checked_out_commit=%s\n' "$(git rev-parse HEAD)"
printf 'sparse_paths:\n'; git sparse-checkout list
printf '.git_bytes=%s\nworking_tree_bytes=%s\nlfs_payload_objects=%s\nlfs_payload_bytes=%s\nelapsed_seconds=%s\n' \
  "$(du_bytes .git)" "$(du_bytes .)" "$lfs_count" "$lfs_bytes" "$elapsed"
