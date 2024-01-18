"""The PerformanceAnalytics table.DownsideRisk function."""
from __future__ import annotations

import pandas as pd

from ..backend.backend import Backend
from ..backend.R.table.downside_risk import DownsideRisk as RDownsideRisk


def DownsideRisk(
    R: pd.DataFrame,
    ci: float = 0.95,
    Rf: (pd.DataFrame | float) = 0.0,
    MAR: float = 0.1 / 12.0,
    p: float = 0.95,
    digits: int = 4,
    backend: Backend = Backend.R,
) -> pd.DataFrame:
    """Calculate table.DownsideRisk."""
    if backend == Backend.R:
        return RDownsideRisk(R, Rf, ci=ci, MAR=MAR, p=p, digits=digits)
    raise NotImplementedError(
        f"Backend {backend.value} not implemented for table.DownsideRisk"
    )
