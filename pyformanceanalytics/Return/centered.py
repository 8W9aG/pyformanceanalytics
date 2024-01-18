"""The PerformanceAnalytics Return.centered function."""
from __future__ import annotations

import pandas as pd

from ..backend.backend import Backend
from ..backend.R.Return.centered import centered as Rcentered


def centered(R: pd.DataFrame, backend: Backend = Backend.R) -> pd.DataFrame:
    """Calculate Return.centered."""
    if backend == Backend.R:
        return Rcentered(R)
    raise NotImplementedError(
        f"Backend {backend.value} not implemented for Return.centered"
    )
