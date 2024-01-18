"""The PerformanceAnalytics UpsideFrequency function."""
from __future__ import annotations

import pandas as pd

from .backend.backend import Backend
from .backend.R.upside_frequency import UpsideFrequency as RUpsideFrequency


def UpsideFrequency(
    R: pd.DataFrame, MAR: float = 0.0, backend: Backend = Backend.R
) -> pd.DataFrame | float:
    """Calculate UpsideFrequency."""
    if backend == Backend.R:
        return RUpsideFrequency(R, MAR=MAR)
    raise NotImplementedError(
        f"Backend {backend.value} not implemented for UpsideFrequency"
    )
