"""The PerformanceAnalytics MinTrackRecord function."""
# pylint: disable=too-many-arguments
from __future__ import annotations

import pandas as pd
from rpy2 import robjects as ro

from .r_df import as_data_frame
from .rimports import PERFORMANCE_ANALYTICS_PACKAGE, ensure_packages_present
from .xts import xts_from_df


def MinTrackRecord(
    refSR: (pd.DataFrame | float),
    Rf: (pd.DataFrame | float),
    R: (pd.DataFrame | None) = None,
    p: float = 0.95,
    weights: (pd.DataFrame | None) = None,
    n: (int | None) = None,
    sr: (float | None) = None,
    sk: (float | None) = None,
    kr: (float | None) = None,
    ignore_skewness: bool = True,
    ignore_kurtosis: bool = True,
) -> pd.DataFrame:
    """Calculate MinTrackRecord."""
    ensure_packages_present([PERFORMANCE_ANALYTICS_PACKAGE])
    with ro.local_context() as lc:
        return as_data_frame(
            ro.r("MinTrackRecord").rcall(  # type: ignore
                (
                    ("R", None if R is None else xts_from_df(R)),
                    ("Rf", xts_from_df(Rf) if isinstance(Rf, pd.DataFrame) else Rf),
                    (
                        "refSR",
                        xts_from_df(refSR)
                        if isinstance(refSR, pd.DataFrame)
                        else refSR,
                    ),
                    ("p", p),
                    (
                        "weights",
                        None if weights is None else xts_from_df(weights),
                    ),
                    ("n", n),
                    ("sr", sr),
                    ("sk", sk),
                    ("kr", kr),
                    ("ignore_skewness", ignore_skewness),
                    ("ignore_kurtosis", ignore_kurtosis),
                ),
                lc,
            ),
            lc,
        )
