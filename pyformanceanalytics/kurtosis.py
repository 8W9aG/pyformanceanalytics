"""The PerformanceAnalytics kurtosis function."""
from __future__ import annotations

import pandas as pd

from .backend.backend import Backend
from .backend.R.kurtosis import kurtosis as Rkurtosis
from .kurtosis_method import KurtosisMethod


def kurtosis(
    x: pd.DataFrame,
    na_rm: bool = False,
    method: (str | KurtosisMethod | None) = None,
    backend: Backend = Backend.R,
) -> pd.DataFrame | float:
    """Calculate kurtosis."""
    if method is None:
        method = KurtosisMethod.MOMENT
    if backend == Backend.R:
        if isinstance(method, KurtosisMethod):
            method = method.value
        return Rkurtosis(x, method, na_rm=na_rm)
    raise NotImplementedError(f"Backend {backend.value} not implemented for kurtosis")
