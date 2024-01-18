"""The PerformanceAnalytics UpsidePotentialRatio function."""
from __future__ import annotations

import pandas as pd

from .backend.backend import Backend
from .backend.R.upside_potential_ratio import \
    UpsidePotentialRatio as RUpsidePotentialRatio
from .upside_potential_ratio_method import UpsidePotentialRatioMethod


def UpsidePotentialRatio(
    R: pd.DataFrame,
    MAR: float = 0.0,
    method: (str | UpsidePotentialRatioMethod | None) = None,
    backend: Backend = Backend.R,
) -> pd.DataFrame:
    """Calculate UpsidePotentialRatio."""
    if method is None:
        method = UpsidePotentialRatioMethod.SUBSET
    if backend == Backend.R:
        if isinstance(method, UpsidePotentialRatioMethod):
            method = method.value
        return RUpsidePotentialRatio(R, method, MAR=MAR)
    raise NotImplementedError(
        f"Backend {backend.value} not implemented for UpsidePotentialRatio"
    )
