"""The PerformanceAnalytics centeredcomoment function."""
from __future__ import annotations

import pandas as pd

from .backend.backend import Backend
from .backend.R.centeredcomoment import centeredcomoment as Rcenteredcomoment


def centeredcomoment(
    Ra: pd.DataFrame,
    Rb: pd.DataFrame,
    p1: float,
    p2: float,
    normalize: bool = False,
    backend: Backend = Backend.R,
) -> pd.DataFrame | float:
    """Calculate centeredcomoment."""
    if backend == Backend.R:
        return Rcenteredcomoment(Ra, Rb, p1, p2, normalize=normalize)
    raise NotImplementedError(
        f"Backend {backend.value} not implemented for centeredcomoment"
    )
