"""The PerformanceAnalytics UpsideRisk function."""
from __future__ import annotations

import pandas as pd

from .backend.backend import Backend
from .backend.R.upside_risk import UpsideRisk as RUpsideRisk


def UpsideRisk(
    R: pd.DataFrame,
    MAR: float = 0.0,
    method: (str | None) = None,
    stat: (str | None) = None,
    backend: Backend = Backend.R,
) -> pd.DataFrame | float:
    """Calculate UpsideRisk."""
    if backend == Backend.R:
        return RUpsideRisk(R, MAR=MAR, method=method, stat=stat)
    raise NotImplementedError(f"Backend {backend.value} not implemented for UpsideRisk")
