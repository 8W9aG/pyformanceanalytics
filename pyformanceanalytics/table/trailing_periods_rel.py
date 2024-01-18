"""The PerformanceAnalytics table.TrailingPeriodsRel function."""
from __future__ import annotations

import pandas as pd

from ..backend.backend import Backend
from ..backend.R.table.trailing_periods_rel import \
    TrailingPeriodsRel as RTrailingPeriodsRel


def TrailingPeriodsRel(
    R: pd.DataFrame,
    Rb: pd.DataFrame,
    periods: (list[int] | None) = None,
    funcs_names: (list[str] | None) = None,
    digits: int = 4,
    backend: Backend = Backend.R,
) -> pd.DataFrame:
    """Calculate table.TrailingPeriodsRel."""
    if backend == Backend.R:
        return RTrailingPeriodsRel(
            R, Rb, periods=periods, funcs_names=funcs_names, digits=digits
        )
    raise NotImplementedError(
        f"Backend {backend.value} not implemented for table.TrailingPeriodsRel"
    )
