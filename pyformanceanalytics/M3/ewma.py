"""The PerformanceAnalytics M3.ewma function."""
from __future__ import annotations

import numpy as np
import pandas as pd

from ..backend.backend import Backend
from ..backend.R.M3.ewma import ewma as Rewma


def ewma(
    R: pd.DataFrame,
    lambda_: float = 0.97,
    last_m3: (np.ndarray | None) = None,
    as_mat: bool = True,
    backend: Backend = Backend.R,
) -> np.ndarray:
    """Calculate M3.ewma."""
    if backend == Backend.R:
        return Rewma(R, lambda_=lambda_, last_m3=last_m3, as_mat=as_mat)
    raise NotImplementedError(f"Backend {backend.value} not implemented for M3.ewma")
