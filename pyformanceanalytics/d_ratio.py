"""The PerformanceAnalytics DRatio function."""
from __future__ import annotations

import pandas as pd

from .backend.backend import Backend
from .backend.R.d_ratio import DRatio as RDRatio


def DRatio(R: pd.DataFrame, backend: Backend = Backend.R) -> pd.DataFrame | float:
    """Calculate DRatio."""
    if backend == Backend.R:
        return RDRatio(R)
    raise NotImplementedError(f"Backend {backend.value} not implemented for DRatio")
