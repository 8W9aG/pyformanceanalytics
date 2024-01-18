"""The PerformanceAnalytics Return.locScaleRob function."""
from __future__ import annotations

import pandas as pd

from ..backend.backend import Backend
from ..backend.R.Return.loc_scale_rob import locScaleRob as RlocScaleRob


def locScaleRob(
    R: pd.DataFrame,
    alpha_robust: float = 0.05,
    normal_efficiency: float = 0.99,
    backend: Backend = Backend.R,
) -> pd.DataFrame:
    """Calculate Return.locScaleRob."""
    if backend == Backend.R:
        return RlocScaleRob(
            R, alpha_robust=alpha_robust, normal_efficiency=normal_efficiency
        )
    raise NotImplementedError(
        f"Backend {backend.value} not implemented for Return.locScaleRob"
    )
