# Fast Git workflow

**Status:** REVIEW. This is an operational workflow for lightweight repository iteration; it does not change scientific files, Git history, or Git LFS tracking.

## Lane A — normal research/Codex iteration

Create a *new* lightweight working copy (changing settings in an existing heavy clone does not remove the objects it already downloaded):

```bash
scripts/git_fast_clone.sh /path/to/French_exporters-fast master
cd /path/to/French_exporters-fast
scripts/git_fast_sync.sh master
```

An optional ref follows the destination, and `--repo-url URL` (or `FAST_GIT_REPO_URL`) selects a different remote. The clone script uses `--filter=blob:none`, `--depth=1`, `--sparse`, and `--no-tags`, then enables only `AGENTS.md`, `research/`, `scripts/`, `docs/`, the two active notebook directories, and `Notes/`. It deliberately uses a non-cone sparse specification because it must include both an individual top-level file and selected nested directories.

The scripts export `GIT_LFS_SKIP_SMUDGE=1` and set clone-local pass-through LFS filters. Therefore normal clone, checkout, fetch, merge, and sync operations do not download LFS payloads. They fail rather than falling back to a full checkout when the partial-clone/promisor, blob filter, sparse checkout, or shallow state is absent.

`git_fast_sync.sh` refuses a dirty tree unless `--allow-dirty` is supplied. It fetches only the requested branch at depth 20, fast-forwards when ancestry is available, and deepens that same branch in bounded increments only when a shallow boundary prevents determining the merge base. It never invokes `git lfs pull`.

## Lane B — selected data work

Only the PI or an explicitly authorized data workflow should hydrate a verified required LFS path. First confirm that the path exists and is the intended tracked artifact, then use the path-specific pattern:

```bash
git lfs pull --include="data/processed/ID_Y.csv" --exclude=""
```

The example is a pattern, not a claim that this exact path is currently available or should be downloaded. Do not use an unbounded `git lfs pull` for normal iteration.

## Lane C — archive/full-history work

Use the existing full clone or a conventional clone only for repository archaeology, data-migration planning, or history-cleanup planning. This lane can require historical Git blobs, all paths, old commits, and potentially LFS payloads, so it is intentionally outside the emergency iteration path.

## What each control does (and does not do)

* `--filter=blob:none` makes Git obtain commit/tree metadata first and fetches ordinary Git blobs only when a checked-out path needs them.
* `--depth=1` limits reachable history initially. It can prevent merge-base discovery, blame, access to older commits, and broad archaeology; use the sync script's incremental deepening rather than immediately unshallowing.
* Sparse checkout limits the working tree to the approved active surface. It does not erase historical objects in an existing clone.
* `GIT_LFS_SKIP_SMUDGE=1` avoids automatic LFS payload hydration. It is distinct from Git's ordinary blob filtering.

A fresh lightweight clone is the preferred emergency remedy because an existing 761 MB-class clone remains large after configuration changes. A later history rewrite or clean replication repository is a separate PI decision, not an action performed by this workflow.

## Verification

Run the isolated integration check (it creates and deletes a temporary clone):

```bash
scripts/verify_fast_git_workflow.sh
```

Set `FAST_GIT_TEST_REF` to verify a supplied reachable branch. The default is `master`; the historical `agent/export-alpha-code-map` reference was not advertised by the remote during the recorded verification, so it is not the default test target.
