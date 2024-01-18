"""The PerformanceAnalytics CAPM RiskPremium function."""
from __future__ import annotations

import pandas as pd

from ..backend.backend import Backend
from ..backend.R.CAPM.risk_premium import RiskPremium as RRiskPremium


def RiskPremium(
    Ra: pd.DataFrame, Rf: (pd.DataFrame | float) = 0.0, backend: Backend = Backend.R
) -> pd.DataFrame:
    """Calculate risk premium."""
    if backend == Backend.R:
        return RRiskPremium(Ra, Rf)
    raise NotImplementedError(
        f"Backend {backend.value} not implemented for CAPM.RiskPremium"
    )
