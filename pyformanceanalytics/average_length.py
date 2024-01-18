"""The PerformanceAnalytics average length function."""
from __future__ import annotations

import pandas as pd

from .backend.backend import Backend
from .backend.R.average_length import AverageLength as RAverageLength


def AverageLength(
    R: pd.DataFrame, backend: Backend = Backend.R
) -> pd.DataFrame | float:
    """Calculate AverageLength."""
    if backend == Backend.R:
        return RAverageLength(R)
    raise NotImplementedError(
        f"Backend {backend.value} not implemented for AverageLength"
    )
