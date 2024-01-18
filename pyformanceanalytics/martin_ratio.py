"""The PerformanceAnalytics MartinRatio function."""
from __future__ import annotations

import pandas as pd

from .backend.backend import Backend
from .backend.R.martin_ratio import MartinRatio as RMartinRatio


def MartinRatio(
    R: pd.DataFrame, Rf: (pd.DataFrame | None) = None, backend: Backend = Backend.R
) -> pd.DataFrame:
    """Calculate MartinRatio."""
    if backend == Backend.R:
        return RMartinRatio(R, Rf=Rf)
    raise NotImplementedError(
        f"Backend {backend.value} not implemented for MartinRatio"
    )
