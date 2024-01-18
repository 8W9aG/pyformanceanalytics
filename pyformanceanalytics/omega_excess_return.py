"""The PerformanceAnalytics OmegaExcessReturn function."""
from __future__ import annotations

import pandas as pd

from .backend.backend import Backend
from .backend.R.omega_excess_return import \
    OmegaExcessReturn as ROmegaExcessReturn


def OmegaExcessReturn(
    Ra: pd.DataFrame, Rb: pd.DataFrame, MAR: float = 0.0, backend: Backend = Backend.R
) -> pd.DataFrame | float:
    """Calculate OmegaExcessReturn."""
    if backend == Backend.R:
        return ROmegaExcessReturn(Ra, Rb, MAR=MAR)
    raise NotImplementedError(
        f"Backend {backend.value} not implemented for OmegaExcessReturn"
    )
