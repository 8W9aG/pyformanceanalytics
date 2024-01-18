"""The PerformanceAnalytics Return.calculate function."""
from __future__ import annotations

import pandas as pd

from ..backend.backend import Backend
from ..backend.R.Return.calculate import calculate as Rcalculate
from .calculate_method import CalculateMethod


def calculate(
    prices: pd.DataFrame,
    method: (str | CalculateMethod | None) = None,
    backend: Backend = Backend.R,
) -> pd.DataFrame:
    """Calculate Return.calculate."""
    if method is None:
        method = CalculateMethod.DISCRETE
    if backend == Backend.R:
        if isinstance(method, CalculateMethod):
            method = method.value
        return Rcalculate(prices, method=method)
    raise NotImplementedError(
        f"Backend {backend.value} not implemented for Return.calculate"
    )
