# Git repository iteration report v0.1

**Artifact state:** REVIEW  
**Classification:** derived infrastructure result; no scientific result is asserted.

```yaml
repository: matuteiglesias/French_exporters
tested_at: 2026-07-22T23:41:32Z
tested_ref: master @ 5ec4788f4779bb1dfcc795e3bc093117bb0c61a6
git_version: git version 2.43.0
git_lfs_version: git-lfs/3.4.1 (GitHub; linux amd64; go 1.22.2)
clone_elapsed_seconds: 2
sync_elapsed_seconds: 1
.git_size: 3747840 bytes after clone; 3801088 bytes after sync
working_tree_size: 9347072 bytes
partial_clone_active: true
shallow: true
sparse_checkout_active: true
lfs_payload_objects: 0
lfs_payload_bytes: 0
acceptance_status: PASS
```

## Commands executed

```bash
bash -n scripts/git_fast_clone.sh scripts/git_fast_sync.sh scripts/verify_fast_git_workflow.sh
scripts/verify_fast_git_workflow.sh
git count-objects -vH
git --version
git lfs version
```

The verifier created a temporary clean clone from the GitHub HTTPS remote, selected `master`, checked promisor/blob-filter configuration, shallow state, sparse state, all required sparse directories, absence of the unrelated `data/` directory, absence of LFS payload objects, a bounded sync, and a clean final `git status --porcelain`. It removed the temporary clone on exit.

## Measurements and platform behavior

The run used Linux with Git 2.43.0 and Git LFS 3.4.1. Git's partial-clone promisor setting and `blob:none` filter were active. The selected sparse paths were `AGENTS.md`, `research/`, `scripts/`, `docs/`, `notebooks/02_Statistical_Analysis_and_Modeling/Thesis/`, `notebooks/06_Visualization_and_Presentation/`, and `Notes/`.

A clone-local pass-through LFS filter is configured in addition to `GIT_LFS_SKIP_SMUDGE=1`. This is required on this platform because the inherited system LFS filter treated `research/state/aggregation_reproducibility_inventory_v0_1.csv` as an LFS pointer during checkout even though the checked-out Git blob was non-pointer, making a fresh clone appear dirty. With the clone-local pass-through filter, the fresh clone remained clean and no LFS payload object was created. This is an operational compatibility observation, not a change to `.gitattributes` or LFS tracking.

## Exact earlier warning and resolution

An initial verifier attempt using `agent/export-alpha-code-map` failed before checkout:

```text
fatal: couldn't find remote ref refs/heads/agent/export-alpha-code-map
ERROR: could not fetch requested ref: agent/export-alpha-code-map
```

`git ls-remote --heads` showed `master` and `agent/fast-git-iteration`, but not that historical test branch. The verifier therefore defaults to the reachable `master` branch and accepts `FAST_GIT_TEST_REF` for a supplied reachable branch. This is a bounded test-fixture correction; no remote ref was modified.

## Remaining latency sources and history-weight diagnosis

The sparse active surface still includes current notebook blobs, so notebooks within the two selected directories remain a material working-tree and ordinary-blob cost when checked out. LFS payloads remain excluded unless explicitly requested.

A pre-existing local full clone was available. `git count-objects -vH` reported one pack with 741 objects and `size-pack: 743.62 MiB`; this establishes substantial existing Git object weight. Largest reachable blobs and pre-LFS migration history were **NOT MEASURED**: the available non-fetching `git verify-pack` inspection did not return usable blob rows in this environment, and no historical download was initiated merely to complete the diagnosis.

## Future decision packet — no action taken

| Option | Expected latency benefit | Scientific-provenance effect | Operational risk | Migration cost |
| --- | --- | --- | --- | --- |
| Keep archive history; standardize fast clones | High for new iteration clones; does not shrink archive | Preserves current provenance unchanged | Low and reversible | Low |
| Rewrite history with `git filter-repo` | Potentially high for conventional clones | Changes published object identities; requires carefully preserved archival mapping | High: coordinated force push and downstream disruption | High |
| Freeze archive; create a small replication/publication repository | High for the new repository | Can preserve archive while making selected verified materials explicit | Medium: scope and release decisions require PI authorization | Medium to high |

The first option is the emergency operational path. The latter two require an explicit PI decision and are not implemented here.

Changed: Added fast-clone, fast-sync, verification, documentation, and this REVIEW report.
Validated: Syntax checks and a temporary clean-clone integration verification passed.
Evidence: Commands and measured values above.
Blocked: No blocker for the emergency path; historical export-alpha branch is unavailable as a remote test ref.
Next: Use a new fast clone for the next iteration; supply another reachable branch through `FAST_GIT_TEST_REF` when needed.
Do not open: History rewrite, LFS migration, data hydration, notebook execution, or repository splitting without PI direction.
