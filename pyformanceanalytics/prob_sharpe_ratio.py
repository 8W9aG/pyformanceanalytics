"""The PerformanceAnalytics ProbSharpeRatio function."""
# pylint: disable=duplicate-code
# pylint: disable=too-many-arguments
from __future__ import annotations

import pandas as pd

from .backend.backend import Backend
from .backend.R.prob_sharpe_ratio import ProbSharpeRatio as RProbSharpeRatio


def ProbSharpeRatio(
    refSR: (pd.DataFrame | float),
    R: (pd.DataFrame | None) = None,
    Rf: (pd.DataFrame | float) = 0.0,
    p: float = 0.95,
    weights: (list[float] | None) = None,
    n: (int | None) = None,
    sr: (float | None) = None,
    sk: (float | None) = None,
    kr: (float | None) = None,
    ignore_skewness: bool = True,
    ignore_kurtosis: bool = True,
    backend: Backend = Backend.R,
) -> pd.DataFrame:
    """Calculate ProbSharpeRatio."""
    if backend == Backend.R:
        return RProbSharpeRatio(
            refSR,
            Rf,
            R=R,
            p=p,
            weights=weights,
            n=n,
            sr=sr,
            sk=sk,
            kr=kr,
            ignore_skewness=ignore_skewness,
            ignore_kurtosis=ignore_kurtosis,
        )
    raise NotImplementedError(
        f"Backend {backend.value} not implemented for ProbSharpeRatio"
    )
