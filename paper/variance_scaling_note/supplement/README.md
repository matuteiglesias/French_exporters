# Concentration Is Not Scaling: An Exact Decomposition of Aggregate Variance Elasticities

## Scientific boundary

This supplement is a deterministic algebraic verification package. It contains **no empirical French-export data** and makes **no claim about a measured export alpha**.

## Tested environment

Validation used Python 3.12.3 on Linux 6.12.13-x86_64 with glibc 2.39. Direct dependencies were `numpy==2.5.1`, `pandas==3.0.5`, `matplotlib==3.11.1`, and `pytest==9.1.1`.

## Contents

- `src/aggregation_lab/`: exact finite-sample variance accounting and finite-interval scaling decomposition.
- `tests/`: identity tests for the public implementation.
- `research/demos/variance_scaling_identity_demo.py`: fixed-seed deterministic demonstration.
- `requirements.txt`: direct runtime and test dependencies only.

## Setup

```bash
python3.12 -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements.txt
```

## Run the tests

```bash
PYTHONPATH=src python -m pytest -q \
  tests/test_variance_identity.py \
  tests/test_scaling_decomposition.py
```

## Run the demonstration

```bash
PYTHONPATH=src python research/demos/variance_scaling_identity_demo.py
```

The demonstration creates `research/artifacts/variance_scaling_demo_v0_1/` containing variance and scaling component/summary CSV files, `checks.csv`, a README, and three PNG diagnostic figures. These generated outputs are not distributed in this portable source supplement.

## Expected numerical checks

All checks must pass with maximum residuals no larger than: variance identity `1e-12`, scaling identity `1e-10`, and designed-versus-measured covariance `1e-12`. The fixed-seed reference run reports:

- variance identity: `4.441e-16`;
- scaling identity: `1.221e-15`;
- designed-versus-measured covariance: `5.551e-16`.

Output values may differ only at normal floating-point precision.

## License

License status: **not specified**.
