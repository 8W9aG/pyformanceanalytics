"""The PerformanceAnalytics UpsidePotentialRatio function."""
from __future__ import annotations

import pandas as pd

from .backend.backend import Backend
from .backend.R.upside_potential_ratio import \
    UpsidePotentialRatio as RUpsidePotentialRatio


def UpsidePotentialRatio(
    R: pd.DataFrame,
    MAR: float = 0.0,
    method: (str | None) = None,
    backend: Backend = Backend.R,
) -> pd.DataFrame:
    """Calculate UpsidePotentialRatio."""
    if backend == Backend.R:
        return RUpsidePotentialRatio(R, MAR=MAR, method=method)
    raise NotImplementedError(
        f"Backend {backend.value} not implemented for UpsidePotentialRatio"
    )
