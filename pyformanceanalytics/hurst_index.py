"""The PerformanceAnalytics HurstIndex function."""
from __future__ import annotations

import pandas as pd

from .backend.backend import Backend
from .backend.R.hurst_index import HurstIndex as RHurstIndex


def HurstIndex(R: pd.DataFrame, backend: Backend = Backend.R) -> pd.DataFrame:
    """Calculate HurstIndex."""
    if backend == Backend.R:
        return RHurstIndex(R)
    raise NotImplementedError(f"Backend {backend.value} not implemented for HurstIndex")
