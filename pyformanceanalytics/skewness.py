"""The PerformanceAnalytics skewness function."""
from __future__ import annotations

import pandas as pd

from .backend.backend import Backend
from .backend.R.skewness import skewness as Rskewness
from .skewness_method import SkewnessMethod


def skewness(
    x: pd.DataFrame,
    na_rm: bool = False,
    method: (str | SkewnessMethod | None) = None,
    backend: Backend = Backend.R,
) -> pd.DataFrame | float:
    """Calculate skewness."""
    if method is None:
        method = SkewnessMethod.MOMENT
    if backend == Backend.R:
        if isinstance(method, SkewnessMethod):
            method = method.value
        return Rskewness(x, na_rm=na_rm, method=method)
    raise NotImplementedError(f"Backend {backend.value} not implemented for skewness")
