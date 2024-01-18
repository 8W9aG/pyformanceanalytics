"""The PerformanceAnalytics calmar ratio function."""
from __future__ import annotations

import pandas as pd

from .backend.backend import Backend
from .backend.R.calmar_ratio import CalmarRatio as RCalmarRatio


def CalmarRatio(R: pd.DataFrame, backend: Backend = Backend.R) -> pd.DataFrame:
    """Calculate CalmarRatio."""
    if backend == Backend.R:
        return RCalmarRatio(R)
    raise NotImplementedError(
        f"Backend {backend.value} not implemented for CalmarRatio"
    )
