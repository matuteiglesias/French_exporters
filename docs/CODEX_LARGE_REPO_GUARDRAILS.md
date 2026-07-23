# Codex Large-Repository Guardrails

**State:** REVIEW  
**Repository:** `matuteiglesias/French_exporters`

These rules apply to every Codex engineering task unless a later PI-authorized task explicitly overrides one item.

## Default operating lane

Work in the currently provided checkout. Treat the checkout as a constrained research surface, not as an invitation to hydrate or duplicate the archive.

Before editing, read:

- `AGENTS.md`
- `docs/FAST_GIT_WORKFLOW.md`
- the task packet named in the prompt

## Hard prohibitions

Do not run or trigger:

```text
git fetch --all
git fetch --unshallow
git pull --rebase --autostash
git lfs pull
git lfs fetch --all
git checkout data/
git add -A
git add .
git gc --aggressive
git repack -a
git filter-repo
git filter-branch
```

Do not:

- clone the repository again inside the repository;
- copy, archive, zip, tar, or vendor the repository tree;
- copy legacy notebooks or data into a new scaffold;
- traverse `.git/objects`, `.git/lfs`, or all historical commits unless the task explicitly authorizes archive work;
- create or modify a remote repository;
- rewrite history, force-push, delete refs, migrate LFS objects, or change `.gitattributes`;
- hydrate any data or LFS pointer unless the PI authorizes the exact path;
- execute notebooks during design, scaffolding, or provenance-only tasks.

## Path and change budget

Every task must declare permitted read and write paths.

Before committing, report:

```bash
git status --short
git diff --stat
git diff --check
```

Unless the task says otherwise, stop for review when any of these limits would be exceeded:

- 40 changed files;
- 1 MiB of new non-lockfile text;
- any binary file;
- any data file;
- any notebook modification;
- any generated environment directory such as `.venv/`, `node_modules/`, build output, cache, or coverage payload.

Use explicit `git add <path>...`; never stage the whole tree.

## Environment rules

- Prefer inspecting existing dependency files before adding another tool.
- Do not install dependencies globally.
- Do not commit virtual environments or caches.
- A setup script may create a local environment, but it must be idempotent and must keep generated files ignored.
- Network-dependent installation is not proof of reproducibility. Record the command and failure if unavailable.
- Tests must have a cheap no-data lane.

## New-project and clean-repository rule

A Codex task in this repository may prepare a **clean export bundle** containing selected text/code files and a migration manifest. It may not assume authority to create a GitHub repository or push to a new remote.

The safe handoff is:

```text
current repository
→ reviewed clean export bundle
→ PI creates empty GitHub repository
→ bundle imported as initial commit
→ separate Codex environment created for the new repository
```

## Completion report

End every task with:

```text
Changed:
Validated:
Evidence:
Blocked:
Next:
Do not open:
```
