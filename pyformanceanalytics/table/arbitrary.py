"""The PerformanceAnalytics table.Arbitrary function."""
from __future__ import annotations

import pandas as pd

from ..backend.backend import Backend
from ..backend.R.table.arbitrary import Arbitrary as RArbitrary


def Arbitrary(
    R: pd.DataFrame,
    metrics: (list[str] | None) = None,
    metrics_names: (list[str] | None) = None,
    backend: Backend = Backend.R,
) -> pd.DataFrame:
    """Calculate table.Arbitrary."""
    if backend == Backend.R:
        return RArbitrary(R, metrics=metrics, metrics_names=metrics_names)
    raise NotImplementedError(
        f"Backend {backend.value} not implemented for table.Arbitrary"
    )
