"""The PerformanceAnalytics CAPM SML slope function."""
from __future__ import annotations

import pandas as pd

from ...backend.backend import Backend
from ...backend.R.CAPM.SML.slope import slope as Rslope


def slope(
    Rb: pd.DataFrame, Rf: (pd.DataFrame | float) = 0.0, backend: Backend = Backend.R
) -> pd.DataFrame:
    """Calculate slope."""
    if backend == Backend.R:
        return Rslope(Rb, Rf)
    raise NotImplementedError(
        f"Backend {backend.value} not implemented for CAPM.SML.slope"
    )
