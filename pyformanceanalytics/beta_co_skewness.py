"""The PerformanceAnalytics beta co skewness function."""
from __future__ import annotations

import pandas as pd

from .backend.backend import Backend
from .backend.R.beta_co_skewness import BetaCoSkewness as RBetaCoSkewness


def BetaCoSkewness(
    Ra: pd.DataFrame, Rb: pd.DataFrame, backend: Backend = Backend.R
) -> pd.DataFrame | float:
    """Calculate BetaCoSkewness."""
    if backend == Backend.R:
        return RBetaCoSkewness(Ra, Rb)
    raise NotImplementedError(
        f"Backend {backend.value} not implemented for BetaCoSkewness"
    )
