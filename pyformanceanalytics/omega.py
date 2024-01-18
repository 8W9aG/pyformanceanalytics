"""The PerformanceAnalytics Omega function."""
from __future__ import annotations

import pandas as pd

from .backend.backend import Backend
from .backend.R.omega import Omega as ROmega


def Omega(
    R: pd.DataFrame,
    L: float = 0.0,
    method: (str | None) = None,
    output: (str | None) = None,
    Rf: (pd.DataFrame | None) = None,
    SE: bool = False,
    backend: Backend = Backend.R,
) -> pd.DataFrame:
    """Calculate Omega."""
    if backend == Backend.R:
        return ROmega(R, L=L, method=method, output=output, Rf=Rf, SE=SE)
    raise NotImplementedError(f"Backend {backend.value} not implemented for Omega")
