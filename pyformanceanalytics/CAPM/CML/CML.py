"""The PerformanceAnalytics CAPM CML function."""
from __future__ import annotations

import pandas as pd

from ...backend.backend import Backend
from ...backend.R.CAPM.CML.CML import CML as RCML


def CML(
    Ra: pd.DataFrame,
    Rb: pd.DataFrame,
    Rf: (pd.DataFrame | float) = 0.0,
    backend: Backend = Backend.R,
) -> pd.DataFrame | float:
    """Calculate CML."""
    if backend == Backend.R:
        return RCML(Ra, Rb, Rf=Rf)
    raise NotImplementedError(f"Backend {backend.value} not implemented for CAPM.CML")
