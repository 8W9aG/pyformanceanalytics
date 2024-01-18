"""The PerformanceAnalytics table.AnnualizedReturns function."""
from __future__ import annotations

import pandas as pd

from ..backend.backend import Backend
from ..backend.R.table.annualized_returns import \
    AnnualizedReturns as RAnnualizedReturns


def AnnualizedReturns(
    R: pd.DataFrame,
    Rf: (pd.DataFrame | float) = 0.0,
    geometric: bool = True,
    digits: int = 4,
    backend: Backend = Backend.R,
) -> pd.DataFrame:
    """Calculate table.AnnualizedReturns."""
    if backend == Backend.R:
        return RAnnualizedReturns(R, Rf, geometric=geometric, digits=digits)
    raise NotImplementedError(
        f"Backend {backend.value} not implemented for table.AnnualizedReturns"
    )
