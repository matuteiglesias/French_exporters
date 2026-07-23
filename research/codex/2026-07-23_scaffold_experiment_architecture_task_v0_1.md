# Codex Task — Scaffold the Experiment Architecture v0.1

**State:** WAITING FOR PI DESIGN FREEZE

Run only after the lightweight development surface is accepted. Read `AGENTS.md`, `docs/CODEX_LARGE_REPO_GUARDRAILS.md`, and the accepted experiment-design artifacts first.

```yaml
target_artifact:
  - src/aggregation_lab/specs.py
  - src/aggregation_lab/results.py
  - src/aggregation_lab/runner.py
  - experiments/export_alpha/spec_v0_1.yaml
  - tests/test_spec_validation.py
  - tests/test_result_schemas.py
  - docs/EXPERIMENT_ARCHITECTURE.md
permitted_paths:
  read: [AGENTS.md, docs/, research/design/, research/artifacts/export_alpha_framework_integration_v0_1.md, src/aggregation_lab/, tests/, experiments/]
  write: [src/aggregation_lab/, tests/, experiments/export_alpha/, docs/EXPERIMENT_ARCHITECTURE.md]
frozen_scientific_meaning: >
  Implement structure only. Do not select the final alpha estimand, population path,
  partition, covariance convention, fit range, tolerance, or empirical source.
inputs: >
  Accepted design contracts only. Use tiny in-memory fixtures created inside tests;
  no repository data and no notebook outputs.
expected_outputs: >
  Typed/validated experiment specification, canonical run/scenario/component/estimate/check
  schemas, a lazy dependency planner skeleton, and no-data tests.
validation_command: "python -m pytest -q tests/test_spec_validation.py tests/test_result_schemas.py && git diff --check"
forbidden_changes: >
  No scientific operator implementations, data adapters, notebook edits/execution,
  dependency expansion, caching backend, workflow engine, CI, or repository migration.
stop_condition: >
  Stop when one minimal declarative spec validates, produces an execution plan without
  running scientific work, and canonical empty/result fixtures pass schema checks.
```

## Required behavior

- Reject unknown or ambiguous fields instead of silently accepting them.
- Make branch type explicit: `observed`, `resampled`, `synthetic`, or `analytic`.
- Record seeds as fields but implement no simulation yet.
- Keep paper/venue profiles outside the scientific spec.
- Keep the runner backend-free; return a plan object and dependency graph only.
- Do not build a large framework or plugin system.

End with the standard `Changed / Validated / Evidence / Blocked / Next / Do not open` report.
