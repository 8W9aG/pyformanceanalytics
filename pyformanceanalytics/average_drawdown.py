"""The PerformanceAnalytics average drawdown function."""
from __future__ import annotations

import pandas as pd

from .backend.backend import Backend
from .backend.R.average_drawdown import AverageDrawdown as RAverageDrawdown


def AverageDrawdown(
    R: pd.DataFrame, backend: Backend = Backend.R
) -> pd.DataFrame | float:
    """Calculate AverageDrawdown."""
    if backend == Backend.R:
        return RAverageDrawdown(R)
    raise NotImplementedError(
        f"Backend {backend.value} not implemented for AverageDrawdown"
    )
