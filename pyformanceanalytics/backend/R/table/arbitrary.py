"""The PerformanceAnalytics table.Arbitrary function."""
from __future__ import annotations

import pandas as pd
from rpy2 import robjects as ro

from ..r_df import as_data_frame
from ..rimports import PERFORMANCE_ANALYTICS_PACKAGE, ensure_packages_present
from ..xts import xts_from_df


def Arbitrary(
    R: pd.DataFrame,
    metrics: list[str],
    metrics_names: (list[str] | None) = None,
) -> pd.DataFrame:
    """Calculate table.Arbitrary."""
    ensure_packages_present([PERFORMANCE_ANALYTICS_PACKAGE])
    if metrics_names is None:
        metrics_names = ["Average Return", "Standard Deviation"]
    with ro.local_context() as lc:
        return as_data_frame(
            ro.r("table.Arbitrary").rcall(  # type: ignore
                (
                    ("R", xts_from_df(R)),
                    ("metrics", ro.vectors.StrVector(metrics)),
                    ("metricsNames", ro.vectors.StrVector(metrics_names)),
                ),
                lc,
            ),
            lc,
        )
