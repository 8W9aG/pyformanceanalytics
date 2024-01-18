"""The PerformanceAnalytics CalculateReturns function."""
from __future__ import annotations

import pandas as pd

from .backend.backend import Backend
from .backend.R.calculate_returns import CalculateReturns as RCalculateReturns
from .calculate_return_method import CalculateReturnMethod


def CalculateReturns(
    prices: pd.DataFrame,
    method: (str | CalculateReturnMethod | None) = None,
    backend: Backend = Backend.R,
) -> pd.DataFrame | float:
    """Calculate CalculateReturns."""
    if method is None:
        method = CalculateReturnMethod.DISCRETE
    if backend == Backend.R:
        if isinstance(method, CalculateReturnMethod):
            method = method.value
        return RCalculateReturns(prices, method)
    raise NotImplementedError(
        f"Backend {backend.value} not implemented for CalculateReturns"
    )
