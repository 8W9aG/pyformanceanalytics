"""The PerformanceAnalytics SemiDeviation function."""
from __future__ import annotations

import pandas as pd

from .backend.backend import Backend
from .backend.R.semi_deviation import SemiDeviation as RSemiDeviation


def SemiDeviation(
    R: pd.DataFrame, SE: bool = False, backend: Backend = Backend.R
) -> pd.DataFrame:
    """Calculate SemiDeviation."""
    if backend == Backend.R:
        return RSemiDeviation(R, SE=SE)
    raise NotImplementedError(
        f"Backend {backend.value} not implemented for SemiDeviation"
    )
