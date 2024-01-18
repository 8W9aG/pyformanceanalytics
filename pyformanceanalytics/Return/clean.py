"""The PerformanceAnalytics Return.clean function."""
from __future__ import annotations

import pandas as pd

from ..backend.backend import Backend
from ..backend.R.Return.clean import clean as Rclean
from ..chart import Clean


def clean(
    R: pd.DataFrame,
    method: (str | Clean | None) = None,
    alpha: float = 0.01,
    backend: Backend = Backend.R,
) -> pd.DataFrame | float:
    """Calculate Return.clean."""
    if method is None:
        method = Clean.NONE
    if backend == Backend.R:
        if isinstance(method, Clean):
            method = method.value
        return Rclean(R, method, alpha=alpha)
    raise NotImplementedError(
        f"Backend {backend.value} not implemented for Return.clean"
    )
