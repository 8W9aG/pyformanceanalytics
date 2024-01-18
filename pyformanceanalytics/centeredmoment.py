"""The PerformanceAnalytics centeredmoment function."""
from __future__ import annotations

import pandas as pd

from .backend.backend import Backend
from .backend.R.centeredmoment import centeredmoment as Rcenteredmoment


def centeredmoment(
    R: pd.DataFrame, power: float = 2.0, backend: Backend = Backend.R
) -> pd.DataFrame:
    """Calculate centeredmoment."""
    if backend == Backend.R:
        return Rcenteredmoment(R, power=power)
    raise NotImplementedError(
        f"Backend {backend.value} not implemented for centeredmoment"
    )
