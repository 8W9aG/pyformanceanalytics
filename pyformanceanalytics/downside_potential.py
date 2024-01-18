"""The PerformanceAnalytics DownsidePotential function."""
from __future__ import annotations

import pandas as pd

from .backend.backend import Backend
from .backend.R.downside_potential import \
    DownsidePotential as RDownsidePotential


def DownsidePotential(
    R: pd.DataFrame, MAR: float = 0.0, backend: Backend = Backend.R
) -> pd.DataFrame | float:
    """Calculate DownsidePotential."""
    if backend == Backend.R:
        return RDownsidePotential(R, MAR=MAR)
    raise NotImplementedError(
        f"Backend {backend.value} not implemented for DownsidePotential"
    )
