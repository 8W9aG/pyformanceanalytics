"""The PerformanceAnalytics mean.UCL function."""
from __future__ import annotations

import pandas as pd
from rpy2 import robjects as ro

from ..r_df import as_data_frame
from ..rimports import PERFORMANCE_ANALYTICS_PACKAGE, ensure_packages_present
from ..xts import xts_from_df


def UCL(x: pd.DataFrame) -> pd.DataFrame | float:
    """Calculate mean.UCL."""
    ensure_packages_present([PERFORMANCE_ANALYTICS_PACKAGE])
    with ro.local_context() as lc:
        return as_data_frame(
            ro.r("mean.UCL").rcall(  # type: ignore
                (("x", xts_from_df(x)),),
                lc,
            ),
            lc,
        )
