"""The PerformanceAnalytics maxDrawdown function."""
from __future__ import annotations

import pandas as pd

from .backend.backend import Backend
from .backend.R.max_drawdown import maxDrawdown as RmaxDrawdown


def maxDrawdown(
    R: pd.DataFrame,
    weights: (list[float] | None) = None,
    geometric: bool = True,
    invert: bool = True,
    backend: Backend = Backend.R,
) -> pd.DataFrame | float:
    """Calculate maxDrawdown."""
    if backend == Backend.R:
        return RmaxDrawdown(R, weights=weights, geometric=geometric, invert=invert)
    raise NotImplementedError(
        f"Backend {backend.value} not implemented for maxDrawdown"
    )
