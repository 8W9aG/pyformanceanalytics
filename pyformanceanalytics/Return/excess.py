"""The PerformanceAnalytics Return.excess function."""
from __future__ import annotations

import pandas as pd

from ..backend.backend import Backend
from ..backend.R.Return.excess import excess as Rexcess


def excess(
    R: pd.DataFrame, Rf: (pd.DataFrame | float) = 0.0, backend: Backend = Backend.R
) -> pd.DataFrame | float:
    """Calculate Return.excess."""
    if backend == Backend.R:
        return Rexcess(R, Rf)
    raise NotImplementedError(
        f"Backend {backend.value} not implemented for Return.excess"
    )
