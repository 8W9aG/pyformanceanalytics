"""The PerformanceAnalytics SemiVariance function."""
from __future__ import annotations

import pandas as pd

from .backend.backend import Backend
from .backend.R.semi_variance import SemiVariance as RSemiVariance


def SemiVariance(R: pd.DataFrame, backend: Backend = Backend.R) -> pd.DataFrame:
    """Calculate SemiVariance."""
    if backend == Backend.R:
        return RSemiVariance(R)
    raise NotImplementedError(
        f"Backend {backend.value} not implemented for SemiVariance"
    )
