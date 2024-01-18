"""The PerformanceAnalytics active premium function."""
from __future__ import annotations

import pandas as pd

from .backend.backend import Backend
from .backend.R.active_premium import ActivePremium as RActivePremium


def ActivePremium(
    Ra: pd.DataFrame, Rb: pd.DataFrame, backend: Backend = Backend.R
) -> pd.DataFrame | float:
    """Calculate ActivePremium."""
    if backend == Backend.R:
        return RActivePremium(Ra, Rb)
    raise NotImplementedError(
        f"Backend {backend.value} not implemented for ActivePremium"
    )
