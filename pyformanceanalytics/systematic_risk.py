"""The PerformanceAnalytics SystematicRisk function."""
from __future__ import annotations

import pandas as pd

from .backend.backend import Backend
from .backend.R.systematic_risk import SystematicRisk as RSystematicRisk


def SystematicRisk(
    Ra: pd.DataFrame,
    Rb: pd.DataFrame,
    Rf: (pd.DataFrame | None) = None,
    backend: Backend = Backend.R,
) -> pd.DataFrame | float:
    """Calculate SystematicRisk."""
    if backend == Backend.R:
        return RSystematicRisk(Ra, Rb, Rf=Rf)
    raise NotImplementedError(
        f"Backend {backend.value} not implemented for SystematicRisk"
    )
