"""The PerformanceAnalytics MM function."""
from __future__ import annotations

import pandas as pd

from ..backend.backend import Backend
from ..backend.R.M4.MM import MM as RMM


def MM(
    R: pd.DataFrame, as_mat: bool = True, backend: Backend = Backend.R
) -> pd.DataFrame | float:
    """Calculate MM."""
    if backend == Backend.R:
        return RMM(R, as_mat=as_mat)
    raise NotImplementedError(f"Backend {backend.value} not implemented for M4.MM")
