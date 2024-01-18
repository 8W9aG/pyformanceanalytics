"""The PerformanceAnalytics SortinoRatio function."""
from __future__ import annotations

import pandas as pd

from .backend.backend import Backend
from .backend.R.sortino_ratio import SortinoRatio as RSortinoRatio
from .sortino_ratio_threshold import SortinoRatioThreshold


def SortinoRatio(
    R: pd.DataFrame,
    MAR: float = 0.0,
    weights: (pd.DataFrame | None) = None,
    threshold: (str | SortinoRatioThreshold | None) = None,
    SE: bool = False,
    backend: Backend = Backend.R,
) -> pd.DataFrame:
    """Calculate SortinoRatio."""
    if threshold is None:
        threshold = SortinoRatioThreshold.MAR
    if backend == Backend.R:
        if isinstance(threshold, SortinoRatioThreshold):
            threshold = threshold.value
        return RSortinoRatio(R, threshold, MAR=MAR, weights=weights, SE=SE)
    raise NotImplementedError(
        f"Backend {backend.value} not implemented for SortinoRatio"
    )
