"""The PerformanceAnalytics ProspectRatio function."""
from __future__ import annotations

import pandas as pd

from .backend.backend import Backend
from .backend.R.prospect_ratio import ProspectRatio as RProspectRatio


def ProspectRatio(
    R: pd.DataFrame, MAR: float = 0.0, backend: Backend = Backend.R
) -> pd.DataFrame | float:
    """Calculate ProspectRatio."""
    if backend == Backend.R:
        return RProspectRatio(R, MAR=MAR)
    raise NotImplementedError(
        f"Backend {backend.value} not implemented for ProspectRatio"
    )
