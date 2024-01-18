"""The PerformanceAnalytics DrawdownDeviation function."""
from __future__ import annotations

import pandas as pd

from .backend.backend import Backend
from .backend.R.drawdown_deviation import \
    DrawdownDeviation as RDrawdownDeviation


def DrawdownDeviation(R: pd.DataFrame, backend: Backend = Backend.R) -> pd.DataFrame:
    """Calculate DrawdownDeviation."""
    if backend == Backend.R:
        return RDrawdownDeviation(R)
    raise NotImplementedError(
        f"Backend {backend.value} not implemented for DrawdownDeviation"
    )
