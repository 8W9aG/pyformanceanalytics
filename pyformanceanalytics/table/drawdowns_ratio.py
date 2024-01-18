"""The PerformanceAnalytics table.DrawdownsRatio function."""
from __future__ import annotations

import pandas as pd

from ..backend.backend import Backend
from ..backend.R.table.drawdowns_ratio import DrawdownsRatio as RDrawdownsRatio


def DrawdownsRatio(
    R: pd.DataFrame,
    Rf: (pd.DataFrame | float) = 0.0,
    digits: int = 4,
    backend: Backend = Backend.R,
) -> pd.DataFrame:
    """Calculate table.DrawdownsRatio."""
    if backend == Backend.R:
        return RDrawdownsRatio(R, Rf, digits=digits)
    raise NotImplementedError(
        f"Backend {backend.value} not implemented for table.DrawdownsRatio"
    )
