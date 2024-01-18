"""The PerformanceAnalytics MeanAbsoluteDeviation function."""
from __future__ import annotations

import pandas as pd

from .backend.backend import Backend
from .backend.R.mean_absolute_deviation import \
    MeanAbsoluteDeviation as RMeanAbsoluteDeviation


def MeanAbsoluteDeviation(
    R: pd.DataFrame, backend: Backend = Backend.R
) -> pd.DataFrame | float:
    """Calculate MeanAbsoluteDeviation."""
    if backend == Backend.R:
        return RMeanAbsoluteDeviation(R)
    raise NotImplementedError(
        f"Backend {backend.value} not implemented for MeanAbsoluteDeviation"
    )
