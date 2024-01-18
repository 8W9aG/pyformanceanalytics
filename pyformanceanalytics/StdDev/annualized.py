"""The PerformanceAnalytics StdDev.annualized function."""
from __future__ import annotations

import pandas as pd

from ..backend.backend import Backend
from ..backend.R.StdDev.annualized import annualized as Rannualized


def annualized(x: pd.DataFrame, backend: Backend = Backend.R) -> pd.DataFrame:
    """Calculate StdDev.annualized."""
    if backend == Backend.R:
        return Rannualized(x)
    raise NotImplementedError(
        f"Backend {backend.value} not implemented for StdDev.annualized"
    )
