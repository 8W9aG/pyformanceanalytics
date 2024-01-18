"""The PerformanceAnalytics table.Arbitrary function."""
from __future__ import annotations

import pandas as pd

from ..backend.backend import Backend
from ..backend.R.table.arbitrary import Arbitrary as RArbitrary
from .arbitrary_metrics import ArbitraryMetrics


def Arbitrary(
    R: pd.DataFrame,
    metrics: (list[str | ArbitraryMetrics] | None) = None,
    metrics_names: (list[str] | None) = None,
    backend: Backend = Backend.R,
) -> pd.DataFrame:
    """Calculate table.Arbitrary."""
    if metrics is None:
        metrics = [ArbitraryMetrics.MEAN, ArbitraryMetrics.SD]
    if backend == Backend.R:
        return RArbitrary(
            R,
            [x.value if isinstance(x, ArbitraryMetrics) else x for x in metrics],
            metrics_names=metrics_names,
        )
    raise NotImplementedError(
        f"Backend {backend.value} not implemented for table.Arbitrary"
    )
