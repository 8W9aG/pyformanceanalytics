"""The PerformanceAnalytics RachevRatio function."""
from __future__ import annotations

import pandas as pd

from .backend.backend import Backend
from .backend.R.rachev_ratio import RachevRatio as RRachevRatio


def RachevRatio(
    R: pd.DataFrame,
    alpha: float = 0.1,
    beta: float = 0.1,
    rf: float = 0.0,
    SE: bool = False,
    backend: Backend = Backend.R,
) -> pd.DataFrame:
    """Calculate RachevRatio."""
    if backend == Backend.R:
        return RRachevRatio(R, alpha=alpha, beta=beta, rf=rf, SE=SE)
    raise NotImplementedError(
        f"Backend {backend.value} not implemented for RachevRatio"
    )
