"""The PerformanceAnalytics lpm function."""
from __future__ import annotations

import pandas as pd

from .backend.backend import Backend
from .backend.R.lpm import lpm as Rlpm


def lpm(
    R: pd.DataFrame,
    n: int = 2,
    threshold: int = 0,
    about_mean: bool = False,
    SE: bool = False,
    backend: Backend = Backend.R,
) -> pd.DataFrame:
    """Calculate lpm."""
    if backend == Backend.R:
        return Rlpm(R, n=n, threshold=threshold, about_mean=about_mean, SE=SE)
    raise NotImplementedError(f"Backend {backend.value} not implemented for lpm")
