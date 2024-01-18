"""The PerformanceAnalytics Kappa function."""
# ruff: noqa: E741
from __future__ import annotations

import pandas as pd

from .backend.backend import Backend
from .backend.R.kappa import Kappa as RKappa


def Kappa(
    R: pd.DataFrame,
    MAR: float = 0.005,
    l: int = 2,  # noqa: E741
    backend: Backend = Backend.R,
) -> pd.DataFrame | float:
    """Calculate Kappa."""
    if backend == Backend.R:
        return RKappa(R, MAR=MAR, l=l)
    raise NotImplementedError(f"Backend {backend.value} not implemented for Kappa")
