"""The PerformanceAnalytics InformationRatio function."""
from __future__ import annotations

import pandas as pd

from .backend.backend import Backend
from .backend.R.information_ratio import InformationRatio as RInformationRatio


def InformationRatio(
    Ra: pd.DataFrame, Rb: pd.DataFrame, backend: Backend = Backend.R
) -> pd.DataFrame | float:
    """Calculate InformationRatio."""
    if backend == Backend.R:
        return RInformationRatio(Ra, Rb)
    raise NotImplementedError(
        f"Backend {backend.value} not implemented for InformationRatio"
    )
