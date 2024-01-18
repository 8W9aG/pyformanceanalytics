"""The PerformanceAnalytics CAPM alpha function."""
from __future__ import annotations

import pandas as pd

from ..backend.backend import Backend
from ..backend.R.CAPM.alpha import alpha as Ralpha


def alpha(
    Ra: pd.DataFrame,
    Rb: pd.DataFrame,
    Rf: (pd.DataFrame | float) = 0.0,
    backend: Backend = Backend.R,
) -> pd.DataFrame | float:
    """Calculate alpha."""
    if backend == Backend.R:
        return Ralpha(Ra, Rb, Rf)
    raise NotImplementedError(f"Backend {backend.value} not implemented for CAPM.alpha")
