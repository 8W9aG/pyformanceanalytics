"""The PerformanceAnalytics skewness function."""
from __future__ import annotations

import pandas as pd
from rpy2 import robjects as ro

from .r_df import as_data_frame_or_float
from .rimports import PERFORMANCE_ANALYTICS_PACKAGE, ensure_packages_present
from .skewness_method import SkewnessMethod
from .xts import xts_from_df


def skewness(
    x: pd.DataFrame,
    na_rm: bool = False,
    method: (str | SkewnessMethod | None) = None,
) -> pd.DataFrame | float:
    """Calculate skewness."""
    ensure_packages_present([PERFORMANCE_ANALYTICS_PACKAGE])
    if method is None:
        method = SkewnessMethod.MOMENT
    if isinstance(method, SkewnessMethod):
        method = method.value
    with ro.local_context() as lc:
        return as_data_frame_or_float(
            ro.r("skewness").rcall(  # type: ignore
                (
                    ("x", xts_from_df(x)),
                    ("na.rm", na_rm),
                    ("method", method),
                ),
                lc,
            ),
            lc,
        )
