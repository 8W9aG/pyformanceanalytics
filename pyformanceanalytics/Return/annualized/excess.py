"""The PerformanceAnalytics Return.annualized.excess function."""
from __future__ import annotations

import pandas as pd

from ...backend.backend import Backend
from ...backend.R.Return.annualized.excess import excess as Rexcess


def excess(
    Rp: pd.DataFrame,
    Rb: pd.DataFrame,
    geometric: bool = True,
    backend: Backend = Backend.R,
) -> pd.DataFrame:
    """Calculate Return.annualized.excess."""
    if backend == Backend.R:
        return Rexcess(Rp, Rb, geometric=geometric)
    raise NotImplementedError(
        f"Backend {backend.value} not implemented for Return.annualized.excess"
    )
