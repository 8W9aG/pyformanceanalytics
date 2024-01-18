"""The PerformanceAnalytics SkewnessKurtosisRatio function."""
from __future__ import annotations

import pandas as pd

from .backend.backend import Backend
from .backend.R.skewness_kurtosis_ratio import \
    SkewnessKurtosisRatio as RSkewnessKurtosisRatio


def SkewnessKurtosisRatio(
    R: pd.DataFrame, backend: Backend = Backend.R
) -> pd.DataFrame | float:
    """Calculate SkewnessKurtosisRatio."""
    if backend == Backend.R:
        return RSkewnessKurtosisRatio(R)
    raise NotImplementedError(
        f"Backend {backend.value} not implemented for SkewnessKurtosisRatio"
    )
