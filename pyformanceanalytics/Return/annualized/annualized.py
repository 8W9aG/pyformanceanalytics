"""The PerformanceAnalytics Return.annualized function."""
from __future__ import annotations

import pandas as pd

from ...backend.backend import Backend
from ...backend.R.Return.annualized.annualized import annualized as Rannualized


def annualized(
    R: pd.DataFrame, geometric: bool = True, backend: Backend = Backend.R
) -> pd.DataFrame:
    """Calculate Return.annualized."""
    if backend == Backend.R:
        return Rannualized(R, geometric=geometric)
    raise NotImplementedError(
        f"Backend {backend.value} not implemented for Return.annualized"
    )
