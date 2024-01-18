"""The PerformanceAnalytics Frequency function."""
from __future__ import annotations

import pandas as pd

from .backend.backend import Backend
from .backend.R.frequency import Frequency as RFrequency


def Frequency(R: pd.DataFrame, backend: Backend = Backend.R) -> pd.DataFrame | float:
    """Calculate Frequency."""
    if backend == Backend.R:
        return RFrequency(R)
    raise NotImplementedError(f"Backend {backend.value} not implemented for Frequency")
