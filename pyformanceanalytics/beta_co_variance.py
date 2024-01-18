"""The PerformanceAnalytics beta co variants function."""
from __future__ import annotations

import pandas as pd

from .backend.backend import Backend
from .backend.R.beta_co_variance import BetaCoVariance as RBetaCoVariance


def BetaCoVariance(
    Ra: pd.DataFrame, Rb: pd.DataFrame, backend: Backend = Backend.R
) -> pd.DataFrame | float:
    """Calculate BetaCoVariance."""
    if backend == Backend.R:
        return RBetaCoVariance(Ra, Rb)
    raise NotImplementedError(
        f"Backend {backend.value} not implemented for BetaCoVariance"
    )
