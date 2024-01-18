"""The PerformanceAnalytics Return.cumulative function."""
from __future__ import annotations

import pandas as pd

from ..backend.backend import Backend
from ..backend.R.Return.cumulative import cumulative as Rcumulative


def cumulative(
    R: pd.DataFrame, geometric: bool = True, backend: Backend = Backend.R
) -> pd.DataFrame:
    """Calculate Return.cumulative."""
    if backend == Backend.R:
        return Rcumulative(R, geometric=geometric)
    raise NotImplementedError(
        f"Backend {backend.value} not implemented for Return.cumulative"
    )
