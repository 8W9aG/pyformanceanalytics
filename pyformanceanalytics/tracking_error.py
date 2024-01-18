"""The PerformanceAnalytics TrackingError function."""
from __future__ import annotations

import pandas as pd

from .backend.backend import Backend
from .backend.R.tracking_error import TrackingError as RTrackingError


def TrackingError(
    Ra: pd.DataFrame, Rb: pd.DataFrame, backend: Backend = Backend.R
) -> pd.DataFrame | float:
    """Calculate TrackingError."""
    if backend == Backend.R:
        return RTrackingError(Ra, Rb)
    raise NotImplementedError(
        f"Backend {backend.value} not implemented for TrackingError"
    )
