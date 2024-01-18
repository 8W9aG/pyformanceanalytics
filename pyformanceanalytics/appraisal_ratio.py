"""The PerformanceAnalytics appraisal ratio function."""
from __future__ import annotations

import pandas as pd

from .appraisal_ratio_method import AppraisalRatioMethod
from .backend.backend import Backend
from .backend.R.appraisal_ratio import AppraisalRatio as RAppraisalRatio


def AppraisalRatio(
    Ra: pd.DataFrame,
    Rb: pd.DataFrame,
    Rf: (pd.DataFrame | float) = 0.0,
    method: (str | AppraisalRatioMethod | None) = None,
    backend: Backend = Backend.R,
) -> pd.DataFrame | float:
    """Calculate AdjustedSharpeRatio."""
    if method is None:
        method = AppraisalRatioMethod.APPRAISAL
    if backend == Backend.R:
        if isinstance(method, AppraisalRatioMethod):
            method = method.value
        return RAppraisalRatio(Ra, Rb, method, Rf)
    raise NotImplementedError(
        f"Backend {backend.value} not implemented for AppraisalRatio"
    )
