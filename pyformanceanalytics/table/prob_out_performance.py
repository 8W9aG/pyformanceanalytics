"""The PerformanceAnalytics table.ProbOutPerformance function."""
from __future__ import annotations

import pandas as pd

from ..backend.backend import Backend
from ..backend.R.table.prob_out_performance import \
    ProbOutPerformance as RProbOutPerformance


def ProbOutPerformance(
    R: pd.DataFrame,
    Rb: pd.DataFrame,
    period_lengths: (list[int] | None) = None,
    backend: Backend = Backend.R,
) -> pd.DataFrame:
    """Calculate table.ProbOutPerformance."""
    if backend == Backend.R:
        return RProbOutPerformance(R, Rb, period_lengths=period_lengths)
    raise NotImplementedError(
        f"Backend {backend.value} not implemented for table.ProbOutPerformance"
    )
