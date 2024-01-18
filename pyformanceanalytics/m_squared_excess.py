"""The PerformanceAnalytics MSquaredExcess function."""
from __future__ import annotations

import pandas as pd

from .backend.backend import Backend
from .backend.R.m_squared_excess import MSquaredExcess as RMSquaredExcess
from .m_squared_excess_method import MSquaredExcessMethod


def MSquaredExcess(
    Ra: pd.DataFrame,
    Rb: pd.DataFrame,
    Rf: (pd.DataFrame | float) = 0.0,
    method: (str | MSquaredExcessMethod | None) = None,
    backend: Backend = Backend.R,
) -> pd.DataFrame:
    """Calculate MSquaredExcess."""
    if method is None:
        method = MSquaredExcessMethod.GEOMETRIC
    if backend == Backend.R:
        if isinstance(method, MSquaredExcessMethod):
            method = method.value
        return RMSquaredExcess(Ra, Rb, method, Rf)
    raise NotImplementedError(
        f"Backend {backend.value} not implemented for MSquaredExcess"
    )
