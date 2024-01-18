"""The PerformanceAnalytics Return.Geltner function."""
# ruff: noqa: F401
from __future__ import annotations

import pandas as pd

from ..backend.backend import Backend
from ..backend.R.Return.geltner import Geltner as RGeltner


def Geltner(Ra: pd.DataFrame, backend: Backend = Backend.R) -> pd.DataFrame | float:
    """Calculate Return.Geltner."""
    if backend == Backend.R:
        return RGeltner(Ra)
    raise NotImplementedError(
        f"Backend {backend.value} not implemented for Return.Geltner"
    )
