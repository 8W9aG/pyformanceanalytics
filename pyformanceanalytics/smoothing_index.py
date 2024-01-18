"""The PerformanceAnalytics SmoothingIndex function."""
from __future__ import annotations

import pandas as pd

from .backend.backend import Backend
from .backend.R.smoothing_index import SmoothingIndex as RSmoothingIndex


def SmoothingIndex(
    R: pd.DataFrame,
    neg_thetas: bool = False,
    ma_order: int = 2,
    verbose: bool = False,
    backend: Backend = Backend.R,
) -> pd.DataFrame:
    """Calculate SmoothingIndex."""
    if backend == Backend.R:
        return RSmoothingIndex(
            R, neg_thetas=neg_thetas, ma_order=ma_order, verbose=verbose
        )
    raise NotImplementedError(
        f"Backend {backend.value} not implemented for SmoothingIndex"
    )
