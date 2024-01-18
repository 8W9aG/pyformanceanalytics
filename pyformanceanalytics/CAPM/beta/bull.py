"""The PerformanceAnalytics CAPM beta bull function."""
from __future__ import annotations

import pandas as pd

from ...backend.backend import Backend
from ...backend.R.CAPM.beta.bull import bull as Rbull


def bull(
    Ra: pd.DataFrame,
    Rb: pd.DataFrame,
    Rf: (pd.DataFrame | float) = 0.0,
    backend: Backend = Backend.R,
) -> pd.DataFrame | float:
    """Calculate bull."""
    if backend == Backend.R:
        return Rbull(Ra, Rb, Rf)
    raise NotImplementedError(
        f"Backend {backend.value} not implemented for CAPM.beta.bull"
    )
