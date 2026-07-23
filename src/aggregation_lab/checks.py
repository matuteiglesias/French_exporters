"""Small numerical validation helpers used by aggregation accounting."""

import numpy as np


def require_close(actual, expected, *, rtol=1e-10, atol=1e-12, label="values"):
    """Raise ValueError unless values agree under scale-aware tolerances."""
    actual = np.asarray(actual, dtype=float)
    expected = np.asarray(expected, dtype=float)
    if not np.all(np.isfinite(actual)) or not np.all(np.isfinite(expected)):
        raise ValueError(f"{label} must be finite")
    if not np.allclose(actual, expected, rtol=rtol, atol=atol):
        difference = np.max(np.abs(actual - expected))
        scale = np.max(np.maximum(np.abs(actual), np.abs(expected)))
        raise ValueError(
            f"{label} differ (max absolute difference={difference}, scale={scale}, "
            f"rtol={rtol}, atol={atol})"
        )
