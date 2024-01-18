"""The PerformanceAnalytics CAPM beta function."""
from __future__ import annotations

import pandas as pd

from ...backend.backend import Backend
from ...backend.R.CAPM.beta.beta import beta as Rbeta


def beta(
    Ra: pd.DataFrame,
    Rb: pd.DataFrame,
    Rf: (pd.DataFrame | None) = None,
    backend: Backend = Backend.R,
) -> pd.DataFrame | float:
    """Calculate beta."""
    if backend == Backend.R:
        return Rbeta(Ra, Rb, Rf=Rf)
    raise NotImplementedError(f"Backend {backend.value} not implemented for CAPM.beta")
