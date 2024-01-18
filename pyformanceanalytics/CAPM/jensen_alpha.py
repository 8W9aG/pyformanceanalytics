"""The PerformanceAnalytics CAPM jensen alpha function."""
from __future__ import annotations

import pandas as pd

from ..backend.backend import Backend
from ..backend.R.CAPM.jensen_alpha import jensenAlpha as RjensenAlpha


def jensenAlpha(
    Ra: pd.DataFrame,
    Rb: pd.DataFrame,
    Rf: (pd.DataFrame | float) = 0.0,
    backend: Backend = Backend.R,
) -> pd.DataFrame | float:
    """Calculate jensen alpha."""
    if backend == Backend.R:
        return RjensenAlpha(Ra, Rb, Rf)
    raise NotImplementedError(
        f"Backend {backend.value} not implemented for CAPM.jensenAlpha"
    )
