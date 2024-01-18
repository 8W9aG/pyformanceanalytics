"""The PerformanceAnalytics burke ratio function."""
from __future__ import annotations

import pandas as pd

from .backend.backend import Backend
from .backend.R.burke_ratio import BurkeRatio as RBurkeRatio


def BurkeRatio(
    R: pd.DataFrame,
    Rf: (pd.DataFrame | float) = 0.0,
    modified: bool = False,
    backend: Backend = Backend.R,
) -> pd.DataFrame | float:
    """Calculate BurkeRatio."""
    if backend == Backend.R:
        return RBurkeRatio(R, Rf, modified=modified)
    raise NotImplementedError(f"Backend {backend.value} not implemented for BurkeRatio")
