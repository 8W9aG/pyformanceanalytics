"""The PerformanceAnalytics average recovery function."""
from __future__ import annotations

import pandas as pd
from rpy2 import robjects as ro

from .r_df import as_data_frame_or_float
from .rimports import PERFORMANCE_ANALYTICS_PACKAGE, ensure_packages_present
from .xts import xts_from_df


def AverageRecovery(R: pd.DataFrame) -> pd.DataFrame | float:
    """Calculate AverageRecovery."""
    ensure_packages_present([PERFORMANCE_ANALYTICS_PACKAGE])
    with ro.local_context() as lc:
        return as_data_frame_or_float(
            ro.r("AverageRecovery").rcall(  # type: ignore
                (("R", xts_from_df(R)),),
                lc,
            ),
            lc,
        )
