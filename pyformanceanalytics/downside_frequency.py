"""The PerformanceAnalytics DownsideFrequency function."""
from __future__ import annotations

import pandas as pd

from .backend.backend import Backend
from .backend.R.downside_frequency import \
    DownsideFrequency as RDownsideFrequency


def DownsideFrequency(
    R: pd.DataFrame, MAR: float = 0.0, backend: Backend = Backend.R
) -> pd.DataFrame | float:
    """Calculate DownsideFrequency."""
    if backend == Backend.R:
        return RDownsideFrequency(R, MAR=MAR)
    raise NotImplementedError(
        f"Backend {backend.value} not implemented for DownsideFrequency"
    )
