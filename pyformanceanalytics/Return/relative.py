"""The PerformanceAnalytics Return.relative function."""
from __future__ import annotations

import pandas as pd

from ..backend.backend import Backend
from ..backend.R.Return.relative import relative as Rrelative


def relative(
    Ra: pd.DataFrame, Rb: pd.DataFrame, backend: Backend = Backend.R
) -> pd.DataFrame | float:
    """Calculate Return.relative."""
    if backend == Backend.R:
        return Rrelative(Ra, Rb)
    raise NotImplementedError(
        f"Backend {backend.value} not implemented for Return.relative"
    )
