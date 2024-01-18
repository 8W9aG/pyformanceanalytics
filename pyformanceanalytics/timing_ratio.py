"""The PerformanceAnalytics timing ratio function."""
from __future__ import annotations

import pandas as pd

from .backend.backend import Backend
from .backend.R.timing_ratio import TimingRatio as RTimingRatio


def TimingRatio(
    Ra: pd.DataFrame,
    Rb: pd.DataFrame,
    Rf: (pd.DataFrame | None) = None,
    backend: Backend = Backend.R,
) -> pd.DataFrame | float:
    """Calculate TimingRatio."""
    if backend == Backend.R:
        return RTimingRatio(Ra, Rb, Rf=Rf)
    raise NotImplementedError(
        f"Backend {backend.value} not implemented for TimingRatio"
    )
