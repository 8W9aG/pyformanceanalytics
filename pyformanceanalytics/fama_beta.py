"""The PerformanceAnalytics FamaBeta function."""
from __future__ import annotations

import pandas as pd

from .backend.backend import Backend
from .backend.R.fama_beta import FamaBeta as RFamaBeta


def FamaBeta(
    Ra: pd.DataFrame, Rb: pd.DataFrame, backend: Backend = Backend.R
) -> pd.DataFrame:
    """Calculate FamaBeta."""
    if backend == Backend.R:
        return RFamaBeta(Ra, Rb)
    raise NotImplementedError(f"Backend {backend.value} not implemented for FamaBeta")
