"""The PerformanceAnalytics TreynorRatio function."""
from __future__ import annotations

import pandas as pd

from .backend.backend import Backend
from .backend.R.treynor_ratio import TreynorRatio as RTreynorRatio


def TreynorRatio(
    Ra: pd.DataFrame,
    Rb: pd.DataFrame,
    Rf: (pd.DataFrame | float) = 0.0,
    modified: bool = False,
    backend: Backend = Backend.R,
) -> pd.DataFrame | float:
    """Calculate TreynorRatio."""
    if backend == Backend.R:
        return RTreynorRatio(Ra, Rb, Rf, modified=modified)
    raise NotImplementedError(
        f"Backend {backend.value} not implemented for TreynorRatio"
    )
