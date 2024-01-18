"""The PerformanceAnalytics Modigliani function."""
from __future__ import annotations

import pandas as pd

from .backend.backend import Backend
from .backend.R.modigliani import Modigliani as RModigliani


def Modigliani(
    Ra: pd.DataFrame,
    Rb: pd.DataFrame,
    Rf: (pd.DataFrame | float) = 0.0,
    backend: Backend = Backend.R,
) -> pd.DataFrame | float:
    """Calculate Modigliani."""
    if backend == Backend.R:
        return RModigliani(Ra, Rb, Rf)
    raise NotImplementedError(f"Backend {backend.value} not implemented for Modigliani")
