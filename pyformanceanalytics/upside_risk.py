"""The PerformanceAnalytics UpsideRisk function."""
from __future__ import annotations

import pandas as pd

from .backend.backend import Backend
from .backend.R.upside_risk import UpsideRisk as RUpsideRisk
from .upside_risk_method import UpsideRiskMethod
from .upside_risk_stat import UpsideRiskStat


def UpsideRisk(
    R: pd.DataFrame,
    MAR: float = 0.0,
    method: (str | UpsideRiskMethod | None) = None,
    stat: (str | UpsideRiskStat | None) = None,
    backend: Backend = Backend.R,
) -> pd.DataFrame | float:
    """Calculate UpsideRisk."""
    if method is None:
        method = UpsideRiskMethod.FULL
    if stat is None:
        stat = UpsideRiskStat.RISK
    if backend == Backend.R:
        if isinstance(method, UpsideRiskMethod):
            method = method.value
        if isinstance(stat, UpsideRiskStat):
            stat = stat.value
        return RUpsideRisk(R, method, stat, MAR=MAR)
    raise NotImplementedError(f"Backend {backend.value} not implemented for UpsideRisk")
