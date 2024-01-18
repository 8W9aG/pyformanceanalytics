"""The PerformanceAnalytics CDD function."""
from __future__ import annotations

import pandas as pd

from .backend.backend import Backend
from .backend.R.CDD import CDD as RCDD


def CDD(
    R: pd.DataFrame,
    geometric: bool = True,
    invert: bool = True,
    p: float = 0.95,
    backend: Backend = Backend.R,
) -> pd.DataFrame | float:
    """Calculate CDD."""
    if backend == Backend.R:
        return RCDD(R, geometric=geometric, invert=invert, p=p)
    raise NotImplementedError(f"Backend {backend.value} not implemented for CDD")
