"""The PerformanceAnalytics M4.MCA function."""
from __future__ import annotations

import pandas as pd

from ..backend.backend import Backend
from ..backend.R.M4.MCA import MCA as RMCA


def MCA(
    R: pd.DataFrame, k: int = 1, as_mat: bool = True, backend: Backend = Backend.R
) -> pd.DataFrame:
    """Calculate M4.MCA."""
    if backend == Backend.R:
        return RMCA(R, k=k, as_mat=as_mat)
    raise NotImplementedError(f"Backend {backend.value} not implemented for M4.MCA")
