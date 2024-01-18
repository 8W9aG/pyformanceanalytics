"""The PerformanceAnalytics M2.ewma function."""
from __future__ import annotations

import numpy as np
import pandas as pd

from ..backend.backend import Backend
from ..backend.R.M2.ewma import ewma as Rewma


def ewma(
    R: pd.DataFrame,
    lambda_: float = 0.97,
    last_m2: (np.ndarray | None) = None,
    backend: Backend = Backend.R,
) -> pd.DataFrame:
    """Calculate M2.ewma."""
    if backend == Backend.R:
        return Rewma(R, lambda_=lambda_, last_m2=last_m2)
    raise NotImplementedError(f"Backend {backend.value} not implemented for M2.ewma")
