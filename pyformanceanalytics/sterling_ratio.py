"""The PerformanceAnalytics sterling ratio function."""
from __future__ import annotations

import pandas as pd

from .backend.backend import Backend
from .backend.R.sterling_ratio import SterlingRatio as RSterlingRatio


def SterlingRatio(
    R: pd.DataFrame, excess: float = 0.1, backend: Backend = Backend.R
) -> pd.DataFrame:
    """Calculate SterlingRatio."""
    if backend == Backend.R:
        return RSterlingRatio(R, excess=excess)
    raise NotImplementedError(
        f"Backend {backend.value} not implemented for SterlingRatio"
    )
