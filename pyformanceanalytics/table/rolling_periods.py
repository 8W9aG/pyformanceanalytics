"""The PerformanceAnalytics table.RollingPeriods function."""
from __future__ import annotations

import pandas as pd

from ..backend.backend import Backend
from ..backend.R.table.rolling_periods import RollingPeriods as RRollingPeriods


def RollingPeriods(
    R: pd.DataFrame,
    periods: (list[int] | None) = None,
    funcs_names: (list[str] | None) = None,
    digits: int = 4,
    backend: Backend = Backend.R,
) -> pd.DataFrame:
    """Calculate table.RollingPeriods."""
    if backend == Backend.R:
        return RRollingPeriods(
            R, periods=periods, funcs_names=funcs_names, digits=digits
        )
    raise NotImplementedError(
        f"Backend {backend.value} not implemented for table.RollingPeriods"
    )
