"""The PerformanceAnalytics timing ratio function."""
from __future__ import annotations

import pandas as pd

from .backend.backend import Backend
from .backend.R.timing_ratio import TimingRatio as RTimingRatio


def TimingRatio(
    Ra: pd.DataFrame,
    Rb: pd.DataFrame,
    Rf: (pd.DataFrame | float) = 0.0,
    backend: Backend = Backend.R,
) -> pd.DataFrame | float:
    """Calculate TimingRatio."""
    if backend == Backend.R:
        return RTimingRatio(Ra, Rb, Rf)
    raise NotImplementedError(
        f"Backend {backend.value} not implemented for TimingRatio"
    )
