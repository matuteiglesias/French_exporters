# Task specification — variance scaling demonstration v0.2

```yaml
target_artifact: research/artifacts/variance_scaling_demo_v0_2/
permitted_paths:
  - research/demos/variance_scaling_identity_demo.py
  - research/artifacts/variance_scaling_demo_v0_2/
  - research/codex/2026-07-24_variance_scaling_demo_v0_2_task.md
  - src/tests/test_variance_scaling_demo.py
frozen_scientific_meaning: >-
  Deterministic algebraic demonstration only. The user-specified equal-weight,
  equicorrelated construction uses H(N)=1/N and V(N)=rho+(1-rho)/N for rho=0.15;
  its finite-interval alpha is decomposed into diagonal and covariance categories.
inputs:
  - User-specified N grid [4, 8, 16, 32, 64] and analytic covariance paths
  - Existing public aggregation_lab variance and scaling APIs
expected_outputs:
  - Versioned machine-readable summaries, components, and checks for v0.2
  - Three figures generated locally but ignored from Git
  - README with provenance, residuals, and failure-report status
validation_command: >-
  PYTHONPATH=src python research/demos/variance_scaling_identity_demo.py &&
  PYTHONPATH=src pytest -q src/tests/test_variance_scaling_demo.py src/tests/test_scaling_decomposition.py
forbidden_changes:
  - Legacy notebook edits
  - Modification or deletion of v0.1 artifacts
  - Empirical-data claims, sample changes, or estimation claims
  - Committing binary image files
stop_condition: >-
  v0.2 checks pass; its covariance category has negative alpha contributions;
  no PNG/PDF is staged; otherwise record the first failure in the v0.2 README.
```

## v0.2 CSV-contract amendment

```yaml
target_artifact: research/artifacts/variance_scaling_demo_v0_2/
permitted_paths:
  - research/demos/variance_scaling_identity_demo.py
  - research/artifacts/variance_scaling_demo_v0_2/
  - research/codex/2026-07-24_variance_scaling_demo_v0_2_task.md
  - src/tests/test_variance_scaling_demo.py
frozen_scientific_meaning: >-
  The three specified deterministic scenarios and their formulas are unchanged.
  This amendment only makes the produced audit tables self-explanatory; it does
  not alter an estimand, sample, or empirical claim.
inputs:
  - Existing analytic v0.2 scenario accounting and scaling-decomposition outputs
expected_outputs:
  - scenario_metadata.csv, path_summary.csv, interval_summary.csv, and
    component_interval_summary.csv with the specified CSV contract
  - checks.csv using the scale-aware acceptance formula from aggregation_lab
validation_command: >-
  PYTHONPATH=src:. pytest -q src/tests/test_variance_scaling_demo.py &&
  PYTHONPATH=src python research/demos/variance_scaling_identity_demo.py
forbidden_changes:
  - Modification or deletion of v0.1 artifacts
  - Alteration of scenario formulas or scientific interpretation
  - Committing PNG, PDF, or other binary files
stop_condition: >-
  All new contract tables are generated and tested, Scenario 1 appears in the
  interval summary, and no binary file is staged.
```

## v0.2 figure-contract amendment

```yaml
target_artifact: research/artifacts/variance_scaling_demo_v0_2/
permitted_paths:
  - research/demos/variance_scaling_identity_demo.py
  - research/artifacts/variance_scaling_demo_v0_2/README.md
  - research/codex/2026-07-24_variance_scaling_demo_v0_2_task.md
  - src/tests/test_variance_scaling_demo.py
frozen_scientific_meaning: >-
  The scenario formulas, population grid, and deterministic accounting are
  unchanged. This amendment changes only the local review-figure presentation.
inputs:
  - Existing v0.2 path, interval, and component-interval contract outputs
expected_outputs:
  - Figure 1 with concentration/variance levels and finite-interval elasticities
  - Figure 2 with heterogeneous and correlated component attribution panels
validation_command: >-
  PYTHONPATH=src:. pytest -q src/tests/test_variance_scaling_demo.py &&
  PYTHONPATH=src python research/demos/variance_scaling_identity_demo.py
forbidden_changes:
  - Scenario or estimand changes
  - Committing PNG, PDF, or any binary figure
stop_condition: >-
  The two locally generated review figures implement the stated marks, labels,
  zero line, and computed residual annotation; no binary is staged.
```
