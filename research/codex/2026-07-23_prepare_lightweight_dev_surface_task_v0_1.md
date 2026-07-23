# Codex Task — Prepare a Lightweight Development Surface v0.1

**State:** READY FOR CODEX

Read `AGENTS.md`, `docs/FAST_GIT_WORKFLOW.md`, and `docs/CODEX_LARGE_REPO_GUARDRAILS.md` first.

```yaml
target_artifact:
  - pyproject.toml
  - Makefile
  - src/aggregation_lab/__init__.py
  - tests/test_smoke.py
  - scripts/setup_lightweight_dev.sh
  - docs/LIGHTWEIGHT_DEV_ENV.md
permitted_paths:
  read: [AGENTS.md, docs/, scripts/, research/design/, pyproject.toml, requirements.txt, setup.py, setup.cfg, Makefile, .gitignore]
  write: [pyproject.toml, Makefile, src/aggregation_lab/, tests/test_smoke.py, scripts/setup_lightweight_dev.sh, docs/LIGHTWEIGHT_DEV_ENV.md, .gitignore]
frozen_scientific_meaning: "Infrastructure only; define no scientific defaults, estimands, partitions, or alpha conventions."
inputs: "Existing configuration only. No data, notebook execution, or legacy-code copying."
expected_outputs: "Minimal installable Python package shell, idempotent setup script, cheap no-data smoke test, and documented commands."
validation_command: "bash -n scripts/setup_lightweight_dev.sh && python -m compileall -q src tests && python -m pytest -q tests/test_smoke.py && git diff --check"
forbidden_changes: "No data/LFS access, notebook edits, broad dependency upgrades, CI, environment lockfiles, archive copying, history work, or remote creation."
stop_condition: "Stop when the no-data smoke test passes or at the first precise dependency failure."
```

## Design constraints

- Keep runtime dependencies empty unless an inspected existing requirement proves one is necessary.
- Put optional development dependencies in one clearly named extra.
- The setup script may create `.venv`, but must not commit it and must be safe to rerun.
- Do not scan the whole repository to discover Python code.
- Do not import legacy notebooks or data from the smoke test.
- Use explicit `git add` paths only.

End with:

```text
Changed:
Validated:
Evidence:
Blocked:
Next:
Do not open:
```
