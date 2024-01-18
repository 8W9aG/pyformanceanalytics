"""The PerformanceAnalytics average recovery function."""
from __future__ import annotations

import pandas as pd

from .backend.backend import Backend
from .backend.R.average_recovery import AverageRecovery as RAverageRecovery


def AverageRecovery(
    R: pd.DataFrame, backend: Backend = Backend.R
) -> pd.DataFrame | float:
    """Calculate AverageRecovery."""
    if backend == Backend.R:
        return RAverageRecovery(R)
    raise NotImplementedError(
        f"Backend {backend.value} not implemented for AverageRecovery"
    )
