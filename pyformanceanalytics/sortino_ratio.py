"""The PerformanceAnalytics SortinoRatio function."""
from __future__ import annotations

import pandas as pd

from .backend.backend import Backend
from .backend.R.sortino_ratio import SortinoRatio as RSortinoRatio


def SortinoRatio(
    R: pd.DataFrame,
    MAR: float = 0.0,
    weights: (pd.DataFrame | None) = None,
    threshold: (str | None) = None,
    SE: bool = False,
    backend: Backend = Backend.R,
) -> pd.DataFrame:
    """Calculate SortinoRatio."""
    if backend == Backend.R:
        return RSortinoRatio(R, MAR=MAR, weights=weights, threshold=threshold, SE=SE)
    raise NotImplementedError(
        f"Backend {backend.value} not implemented for SortinoRatio"
    )
