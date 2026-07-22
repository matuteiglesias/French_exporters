# Codex task — emergency fast Git iteration v0.1

## Priority

**Emergency infrastructure gate. Pause scientific implementation until this task has a usable fast path.**

The repository is approximately 761 MB and contains large historical data artifacts plus Git LFS-managed CSVs. Full clone, fetch, checkout, and workspace synchronization are too slow for tight research iteration.

The immediate goal is **not** to rewrite repository history. The immediate goal is to create a safe lightweight working path for Codex, the Steward, and the PI.

## Authority and scope

Follow `AGENTS.md`.

```yaml
target_artifact:
  - scripts/git_fast_clone.sh
  - scripts/git_fast_sync.sh
  - scripts/verify_fast_git_workflow.sh
  - docs/FAST_GIT_WORKFLOW.md
  - research/artifacts/git_repository_iteration_report_v0_1.md
permitted_paths:
  - scripts/
  - docs/
  - research/artifacts/
  - research/codex/2026-07-23_fast_git_iteration_task_v0_1.md
frozen_scientific_meaning: "No scientific estimand, code, notebook, output, or data meaning may change."
inputs:
  - repository metadata and Git configuration
  - Git and Git LFS command behavior
  - current directory structure
expected_outputs: "A tested partial-clone, sparse-checkout, LFS-skip workflow and a measured infrastructure report."
forbidden_changes:
  - no history rewrite
  - no force push
  - no tag deletion
  - no branch deletion
  - no Git LFS migration or untracking
  - no deletion, movement, editing, or execution of data files or scientific notebooks
  - no change to .gitattributes
  - no repository split or creation of a replacement repository
  - no package/environment modernization
stop_condition: "A fresh lightweight clone can fetch and check out a selected research branch without downloading LFS payloads, scripts pass syntax checks, and measurements plus residual limitations are recorded."
```

## Problem definition

There are two separate problems. Do not conflate them.

1. **Iteration latency now:** new working copies and Codex environments should avoid downloading old blobs, irrelevant directories, notebook outputs, and LFS payloads.
2. **Repository weight in history:** old large Git blobs may remain reachable and make conventional full clones expensive.

Solve problem 1 in this task. Measure and describe problem 2 only where possible without causing a large historical download.

## Required implementation

### 1. `scripts/git_fast_clone.sh`

Create a defensive Bash script that provisions a lightweight clone of this repository.

Required behavior:

- `set -euo pipefail`.
- Accept destination directory and optional branch/ref.
- Default repository URL to `https://github.com/matuteiglesias/French_exporters.git` but allow an environment-variable or argument override.
- Set `GIT_LFS_SKIP_SMUDGE=1` for clone and checkout.
- Use a partial, shallow, sparse clone. Preferred starting command:

  ```bash
  git clone \
    --filter=blob:none \
    --depth=1 \
    --sparse \
    --no-tags \
    "$REPO_URL" "$DEST"
  ```

- Configure sparse checkout for the minimum useful engineering/research surface:

  ```text
  AGENTS.md
  research/
  scripts/
  docs/
  notebooks/02_Statistical_Analysis_and_Modeling/Thesis/
  notebooks/06_Visualization_and_Presentation/
  Notes/
  ```

- Because sparse-checkout mode and individual top-level files have edge cases, implement and test a robust pattern. Non-cone mode is acceptable when justified. Do not silently fall back to a full checkout.
- Fetch and check out the requested branch/ref with the smallest practical refspec and depth.
- Configure the clone so future ordinary `git pull` or checkout actions do not automatically download LFS payloads.
- Print:
  - checked-out commit;
  - active sparse paths;
  - `.git` disk usage;
  - working-tree disk usage;
  - number and size of downloaded LFS objects;
  - elapsed wall time.
- Fail clearly if partial clone, sparse checkout, or requested ref checkout is not active.

### 2. `scripts/git_fast_sync.sh`

Create a script for an existing lightweight clone.

Required behavior:

- `set -euo pipefail`.
- Refuse to run with uncommitted changes unless `--allow-dirty` is explicitly supplied.
- Accept a branch/ref.
- Fetch only the requested ref with a bounded depth, initially `--depth=20` unless a smaller depth is sufficient and tested.
- Preserve `GIT_LFS_SKIP_SMUDGE=1`.
- Fast-forward when possible.
- When a shallow boundary prevents a merge-base or fast-forward, deepen incrementally rather than unshallowing immediately.
- Never run `git lfs pull` automatically.
- Print elapsed time, fetched commit, `.git` disk usage, shallow state, and LFS-object count.

### 3. `scripts/verify_fast_git_workflow.sh`

Create an integration check that uses a temporary directory and cleans it on exit.

Minimum checks:

1. `bash -n` passes for all three scripts.
2. A fresh lightweight clone succeeds.
3. The clone is partial/promisor-enabled.
4. The clone is shallow.
5. Sparse checkout is active.
6. `research/` and the two required notebook directories are available.
7. an unrelated heavy directory is not checked out unless it overlaps the selected paths;
8. no Git LFS payload object is downloaded automatically;
9. fetching and checking out `agent/export-alpha-code-map` or another supplied test branch succeeds;
10. `git status --short` is clean after the test.

The verifier must avoid a conventional full clone.

### 4. `docs/FAST_GIT_WORKFLOW.md`

Document three operational lanes.

#### Lane A — normal research/Codex iteration

Use the fast clone and fast sync scripts. No LFS data.

#### Lane B — selected data work

Explain how the PI can explicitly retrieve one necessary LFS path later, for example:

```bash
git lfs pull --include="data/processed/ID_Y.csv" --exclude=""
```

Do not assume that exact tracked path currently exists; present it as a pattern and require verification before use.

#### Lane C — archive/full-history work

Conventional clone or existing full clone. Use only for repository archaeology, data migration, or history-cleanup planning.

Also explain:

- why `--filter=blob:none`, shallow history, sparse checkout, and `GIT_LFS_SKIP_SMUDGE=1` solve different parts of the problem;
- limits of shallow clones for merge bases, blame, old commits, and broad archaeology;
- how to deepen incrementally;
- that existing heavy clones do not become small merely by changing config;
- why a new lightweight clone is the preferred emergency remedy.

### 5. `research/artifacts/git_repository_iteration_report_v0_1.md`

Record measurements from the verification run:

```yaml
repository: matuteiglesias/French_exporters
tested_at: ISO timestamp
tested_ref: commit or branch
git_version: value
git_lfs_version: value or unavailable
clone_elapsed_seconds: value
sync_elapsed_seconds: value
.git_size: value
working_tree_size: value
partial_clone_active: true|false
shallow: true|false
sparse_checkout_active: true|false
lfs_payload_objects: count
lfs_payload_bytes: value
acceptance_status: PASS|BLOCKED
```

Add:

- commands executed;
- any platform-specific behavior;
- exact failures or warnings;
- remaining latency sources;
- whether current notebook blobs themselves are a material cost even under partial/sparse clone.

## History-weight diagnosis — report only

Do not rewrite history in this task.

When a pre-existing full clone is locally available, it is permitted to inspect its existing object database without fetching more history, for example with `git count-objects`, `git verify-pack`, or `git rev-list` only if those commands do not trigger missing-object downloads.

Record, when safely available:

- largest reachable Git blobs;
- approximate historical pack size;
- whether large files were committed before later Git LFS migration;
- likely benefit and disruption of a future `git filter-repo` cleanup;
- alternative of freezing this repository as an archive and creating a small publication/reproduction repository.

When no full clone is available, state `NOT MEASURED`. Do not make the partial clone download all historical blobs merely to complete this section.

## Decision packet for later — no action now

At the end of the report, compare these future options without implementing them:

1. retain archive history and standardize the fast-clone workflow;
2. rewrite history in place with `git filter-repo` and coordinated force push;
3. preserve this repository as the archival source and create a clean reproduction/publication repository containing only verified code, documentation, and nonrestricted derived artifacts.

For each, state expected latency benefit, scientific-provenance effect, operational risk, and migration cost.

## Acceptance tests

Run and record:

```bash
bash -n scripts/git_fast_clone.sh
bash -n scripts/git_fast_sync.sh
bash -n scripts/verify_fast_git_workflow.sh
scripts/verify_fast_git_workflow.sh
```

Acceptance requires all of the following:

- no legacy scientific or data file changed;
- no history or refs rewritten;
- fresh test clone uses partial clone, shallow history, sparse checkout, and LFS skip;
- no LFS payloads downloaded automatically;
- requested research branch can be fetched and checked out;
- scripts fail with actionable messages rather than silently falling back to a heavy operation;
- report contains measured results or an exact external blocker.

## Handoff

```yaml
from_role: Codex / Infrastructure Engineer
to_role: Steward
artifact:
  - scripts/git_fast_clone.sh
  - scripts/git_fast_sync.sh
  - scripts/verify_fast_git_workflow.sh
  - docs/FAST_GIT_WORKFLOW.md
  - research/artifacts/git_repository_iteration_report_v0_1.md
state: REVIEW
verified: "Only after acceptance commands complete."
open_uncertainties: "Whether a later history rewrite or clean reproduction repository is justified."
decision_needed: "None for emergency fast path; PI decision required before any history rewrite or repository split."
next_action: "Use the fast clone for the next Codex/research iteration and compare observed latency."
stop_condition: "Emergency workflow passes or the first exact Git/GitHub limitation is recorded."
```
