"""The PerformanceAnalytics CAPM epsilon function."""
from __future__ import annotations

import pandas as pd

from ..backend.backend import Backend
from ..backend.R.CAPM.epsilon import epsilon as Repsilon


def epsilon(
    Ra: pd.DataFrame,
    Rb: pd.DataFrame,
    Rf: (pd.DataFrame | float) = 0.0,
    backend: Backend = Backend.R,
) -> pd.DataFrame | float:
    """Calculate epsilon."""
    if backend == Backend.R:
        return Repsilon(Ra, Rb, Rf)
    raise NotImplementedError(
        f"Backend {backend.value} not implemented for CAPM.epsilon"
    )
