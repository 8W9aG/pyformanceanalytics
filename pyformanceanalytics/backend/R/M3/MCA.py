"""The PerformanceAnalytics M3.MCA function."""
from __future__ import annotations

import pandas as pd
from rpy2 import robjects as ro

from ..r_df import as_data_frame
from ..rimports import PERFORMANCE_ANALYTICS_PACKAGE, ensure_packages_present
from ..xts import xts_from_df


def MCA(R: pd.DataFrame, k: int = 1, as_mat: bool = True) -> pd.DataFrame:
    """Calculate M3.MCA."""
    ensure_packages_present([PERFORMANCE_ANALYTICS_PACKAGE])
    with ro.local_context() as lc:
        return as_data_frame(
            ro.r("M3.MCA").rcall(  # type: ignore
                (
                    ("R", xts_from_df(R)),
                    ("k", k),
                    ("as.mat", as_mat),
                ),
                lc,
            ),
            lc,
        )
