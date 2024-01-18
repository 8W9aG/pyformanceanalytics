"""The PerformanceAnalytics PainRatio function."""
from __future__ import annotations

import pandas as pd

from .backend.backend import Backend
from .backend.R.pain_ratio import PainRatio as RPainRatio


def PainRatio(
    R: pd.DataFrame, Rf: (pd.DataFrame | None) = None, backend: Backend = Backend.R
) -> pd.DataFrame:
    """Calculate PainRatio."""
    if backend == Backend.R:
        return RPainRatio(R, Rf=Rf)
    raise NotImplementedError(f"Backend {backend.value} not implemented for PainRatio")
