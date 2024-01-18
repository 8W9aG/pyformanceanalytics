"""The PerformanceAnalytics table.HigherMoments function."""
from __future__ import annotations

import pandas as pd

from ..backend.backend import Backend
from ..backend.R.table.higher_moments import HigherMoments as RHigherMoments


def HigherMoments(
    Ra: pd.DataFrame,
    Rb: pd.DataFrame,
    Rf: (pd.DataFrame | float) = 0.0,
    digits: int = 4,
    method: (str | None) = None,
    backend: Backend = Backend.R,
) -> pd.DataFrame:
    """Calculate table.HigherMoments."""
    if backend == Backend.R:
        return RHigherMoments(Ra, Rb, Rf, digits=digits, method=method)
    raise NotImplementedError(
        f"Backend {backend.value} not implemented for table.HigherMoments"
    )
