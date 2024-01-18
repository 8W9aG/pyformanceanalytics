"""The PerformanceAnalytics MM function."""
from __future__ import annotations

import numpy as np
import pandas as pd

from ..backend.backend import Backend
from ..backend.R.M3.MM import MM as RMM


def MM(
    R: pd.DataFrame,
    unbiased: bool = True,
    as_mat: bool = True,
    backend: Backend = Backend.R,
) -> np.ndarray:
    """Calculate MM."""
    if backend == Backend.R:
        return RMM(R, unbiased=unbiased, as_mat=as_mat)
    raise NotImplementedError(f"Backend {backend.value} not implemented for M3.MM")
