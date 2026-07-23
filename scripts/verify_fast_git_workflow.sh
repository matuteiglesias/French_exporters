#!/usr/bin/env bash
# Integration test for the emergency lightweight Git workflow.
set -euo pipefail

repo_root=$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)
clone_script="$repo_root/scripts/git_fast_clone.sh"
sync_script="$repo_root/scripts/git_fast_sync.sh"
test_ref="${FAST_GIT_TEST_REF:-master}"
tmpdir=$(mktemp -d "${TMPDIR:-/tmp}/french-exporters-fast-git.XXXXXX")
cleanup() { rm -rf "$tmpdir"; }
trap cleanup EXIT

for script in "$clone_script" "$sync_script" "$repo_root/scripts/verify_fast_git_workflow.sh"; do bash -n "$script"; done
"$clone_script" "$tmpdir/clone" "$test_ref"
cd "$tmpdir/clone"
git config --get remote.origin.promisor >/dev/null
git config --get remote.origin.partialclonefilter | grep -qx 'blob:none'
git rev-parse --is-shallow-repository | grep -qx true
git sparse-checkout list >/dev/null
[[ -d research ]] || { echo 'ERROR: research/ missing from sparse checkout' >&2; exit 1; }
[[ -d notebooks/02_Statistical_Analysis_and_Modeling/Thesis ]] || { echo 'ERROR: thesis notebooks missing' >&2; exit 1; }
[[ -d notebooks/06_Visualization_and_Presentation ]] || { echo 'ERROR: visualization notebooks missing' >&2; exit 1; }
# data/ is intentionally outside the approved sparse surface.
[[ ! -e data ]] || { echo 'ERROR: unrelated data/ directory was checked out' >&2; exit 1; }
[[ ! -d .git/lfs/objects ]] || [[ -z "$(find .git/lfs/objects -type f -print -quit)" ]] || { echo 'ERROR: LFS payload downloaded' >&2; exit 1; }
"$sync_script" "$test_ref"
[[ -z "$(git status --porcelain)" ]] || { echo 'ERROR: test clone is dirty' >&2; exit 1; }
printf 'PASS: fast Git clone and sync workflow verified for %s\n' "$test_ref"
