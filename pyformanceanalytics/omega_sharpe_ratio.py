"""The PerformanceAnalytics OmegaSharpeRatio function."""
from __future__ import annotations

import pandas as pd

from .backend.backend import Backend
from .backend.R.omega_sharpe_ratio import OmegaSharpeRatio as ROmegaSharpeRatio


def OmegaSharpeRatio(
    R: pd.DataFrame, MAR: float = 0.0, backend: Backend = Backend.R
) -> pd.DataFrame | float:
    """Calculate OmegaSharpeRatio."""
    if backend == Backend.R:
        return ROmegaSharpeRatio(R, MAR=MAR)
    raise NotImplementedError(
        f"Backend {backend.value} not implemented for OmegaSharpeRatio"
    )
