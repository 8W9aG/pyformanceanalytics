"""The PerformanceAnalytics KellyRatio function."""
from __future__ import annotations

import pandas as pd

from .backend.backend import Backend
from .backend.R.kelly_ratio import KellyRatio as RKellyRatio


def KellyRatio(
    R: pd.DataFrame,
    Rf: (pd.DataFrame | float) = 0.0,
    method: (str | None) = None,
    backend: Backend = Backend.R,
) -> pd.DataFrame:
    """Calculate KellyRatio."""
    if backend == Backend.R:
        return RKellyRatio(R, Rf, method=method)
    raise NotImplementedError(f"Backend {backend.value} not implemented for KellyRatio")
