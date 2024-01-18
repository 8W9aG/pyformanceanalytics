"""The PerformanceAnalytics bernardo ledoit ratio function."""
from __future__ import annotations

import pandas as pd

from .backend.backend import Backend
from .backend.R.bernardo_ledoit_ratio import \
    BernardoLedoitRatio as RBernardoLedoitRatio


def BernardoLedoitRatio(
    R: pd.DataFrame, backend: Backend = Backend.R
) -> pd.DataFrame | float:
    """Calculate BernardoLedoitRatio."""
    if backend == Backend.R:
        return RBernardoLedoitRatio(R)
    raise NotImplementedError(
        f"Backend {backend.value} not implemented for BernardoLedoitRatio"
    )
