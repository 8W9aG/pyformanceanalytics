"""The PerformanceAnalytics table.SFM function."""
from __future__ import annotations

import pandas as pd

from ..backend.backend import Backend
from ..backend.R.table.SFM import SFM as RSFM


def SFM(
    Ra: pd.DataFrame,
    Rb: pd.DataFrame,
    Rf: (pd.DataFrame | float) = 0.0,
    digits: int = 4,
    backend: Backend = Backend.R,
) -> pd.DataFrame:
    """Calculate table.SFM."""
    if backend == Backend.R:
        return RSFM(Ra, Rb, Rf, digits=digits)
    raise NotImplementedError(f"Backend {backend.value} not implemented for table.SFM")
