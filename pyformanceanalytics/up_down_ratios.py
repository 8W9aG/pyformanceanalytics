"""The PerformanceAnalytics UpDownRatios function."""
from __future__ import annotations

import pandas as pd

from .backend.backend import Backend
from .backend.R.up_down_ratios import UpDownRatios as RUpDownRatios


def UpDownRatios(
    Ra: pd.DataFrame,
    Rb: pd.DataFrame,
    method: (str | None) = None,
    side: (str | None) = None,
    backend: Backend = Backend.R,
) -> pd.DataFrame:
    """Calculate UpDownRatios."""
    if backend == Backend.R:
        return RUpDownRatios(Ra, Rb, method=method, side=side)
    raise NotImplementedError(
        f"Backend {backend.value} not implemented for UpDownRatios"
    )
