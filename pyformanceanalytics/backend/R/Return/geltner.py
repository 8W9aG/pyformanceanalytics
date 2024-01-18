"""The PerformanceAnalytics Return.Geltner function."""
# ruff: noqa: F401
from __future__ import annotations

import pandas as pd
from rpy2 import robjects as ro

from ..r_df import as_data_frame_or_float
from ..rimports import PERFORMANCE_ANALYTICS_PACKAGE, ensure_packages_present
from ..xts import xts_from_df


def Geltner(Ra: pd.DataFrame) -> pd.DataFrame | float:
    """Calculate Return.Geltner."""
    ensure_packages_present([PERFORMANCE_ANALYTICS_PACKAGE])
    with ro.local_context() as lc:
        return as_data_frame_or_float(
            ro.r("Return.Geltner").rcall(  # type: ignore
                (("Ra", xts_from_df(Ra)),),
                lc,
            ),
            lc,
        )