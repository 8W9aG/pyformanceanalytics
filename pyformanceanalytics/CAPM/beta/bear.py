"""The PerformanceAnalytics CAPM beta bear function."""
from __future__ import annotations

import pandas as pd

from ...backend.backend import Backend
from ...backend.R.CAPM.beta.bear import bear as Rbear


def bear(
    Ra: pd.DataFrame,
    Rb: pd.DataFrame,
    Rf: (pd.DataFrame | float) = 0.0,
    backend: Backend = Backend.R,
) -> pd.DataFrame | float:
    """Calculate bear."""
    if backend == Backend.R:
        return Rbear(Ra, Rb, Rf)
    raise NotImplementedError(
        f"Backend {backend.value} not implemented for CAPM.beta.bear"
    )
