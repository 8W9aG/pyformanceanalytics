"""The PerformanceAnalytics Return.calculate function."""
from __future__ import annotations

import pandas as pd
from rpy2 import robjects as ro

from ..r_df import as_data_frame
from ..rimports import PERFORMANCE_ANALYTICS_PACKAGE, ensure_packages_present
from ..xts import xts_from_df


def calculate(prices: pd.DataFrame, method: (str | None) = None) -> pd.DataFrame:
    """Calculate Return.calculate."""
    ensure_packages_present([PERFORMANCE_ANALYTICS_PACKAGE])
    with ro.local_context() as lc:
        return as_data_frame(
            ro.r("Return.calculate").rcall(  # type: ignore
                (
                    ("prices", xts_from_df(prices)),
                    ("method", method),
                ),
                lc,
            ),
            lc,
        )
