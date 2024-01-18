"""The PerformanceAnalytics Return.clean function."""
from __future__ import annotations

import pandas as pd

from ..backend.backend import Backend
from ..backend.R.Return.clean import clean as Rclean


def clean(
    R: pd.DataFrame,
    method: (str | None) = None,
    alpha: float = 0.01,
    backend: Backend = Backend.R,
) -> pd.DataFrame | float:
    """Calculate Return.clean."""
    if backend == Backend.R:
        return Rclean(R, method=method, alpha=alpha)
    raise NotImplementedError(
        f"Backend {backend.value} not implemented for Return.clean"
    )
