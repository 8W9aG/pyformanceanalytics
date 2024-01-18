"""The PerformanceAnalytics CAPM dynamic function."""
from __future__ import annotations

import pandas as pd

from ..backend.backend import Backend
from ..backend.R.CAPM.dynamic import dynamic as Rdynamic


def dynamic(
    Ra: pd.DataFrame,
    Rb: pd.DataFrame,
    Z: pd.DataFrame,
    Rf: (pd.DataFrame | float) = 0.0,
    lags: int = 1,
    backend: Backend = Backend.R,
) -> pd.DataFrame | float:
    """Calculate dynamic."""
    if backend == Backend.R:
        return Rdynamic(Ra, Rb, Z, Rf, lags=lags)
    raise NotImplementedError(
        f"Backend {backend.value} not implemented for CAPM.dynamic"
    )
