"""The PerformanceAnalytics beta co kurtosis function."""
from __future__ import annotations

import pandas as pd

from .backend.backend import Backend
from .backend.R.beta_co_kurtosis import BetaCoKurtosis as RBetaCoKurtosis


def BetaCoKurtosis(
    Ra: pd.DataFrame, Rb: pd.DataFrame, backend: Backend = Backend.R
) -> pd.DataFrame | float:
    """Calculate BetaCoKurtosis."""
    if backend == Backend.R:
        return RBetaCoKurtosis(Ra, Rb)
    raise NotImplementedError(
        f"Backend {backend.value} not implemented for BetaCoKurtosis"
    )
