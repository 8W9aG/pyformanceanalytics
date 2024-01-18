"""The PerformanceAnalytics UlcerIndex function."""
from __future__ import annotations

import pandas as pd

from .backend.backend import Backend
from .backend.R.ulcer_index import UlcerIndex as RUlcerIndex


def UlcerIndex(R: pd.DataFrame, backend: Backend = Backend.R) -> pd.DataFrame:
    """Calculate UlcerIndex."""
    if backend == Backend.R:
        return RUlcerIndex(R)
    raise NotImplementedError(f"Backend {backend.value} not implemented for UlcerIndex")
