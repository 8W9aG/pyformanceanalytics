"""The PerformanceAnalytics appraisal ratio function."""
from __future__ import annotations

import pandas as pd

from .backend.backend import Backend
from .backend.R.appraisal_ratio import AppraisalRatio as RAppraisalRatio


def AppraisalRatio(
    Ra: pd.DataFrame,
    Rb: pd.DataFrame,
    Rf: (pd.DataFrame | None) = None,
    method: (str | None) = None,
    backend: Backend = Backend.R,
) -> pd.DataFrame | float:
    """Calculate AdjustedSharpeRatio."""
    if backend == Backend.R:
        return RAppraisalRatio(Ra, Rb, Rf=Rf, method=method)
    raise NotImplementedError(
        f"Backend {backend.value} not implemented for AppraisalRatio"
    )
