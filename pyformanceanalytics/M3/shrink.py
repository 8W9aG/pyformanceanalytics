"""The PerformanceAnalytics M3.shrink function."""
from __future__ import annotations

import pandas as pd
from rpy2 import robjects as ro

from ..r_df import as_data_frame
from ..rimports import PERFORMANCE_ANALYTICS_PACKAGE, ensure_packages_present
from ..xts import xts_from_df


def shrink(
    R: pd.DataFrame,
    targets: int = 1,
    f: (pd.DataFrame | None) = None,
    unbiased_mse: bool = False,
    as_mat: bool = True,
) -> pd.DataFrame:
    """Calculate M3.shrink."""
    ensure_packages_present([PERFORMANCE_ANALYTICS_PACKAGE])
    with ro.local_context() as lc:
        return as_data_frame(
            ro.r("M3.shrink").rcall(  # type: ignore
                (
                    ("R", xts_from_df(R)),
                    ("targets", targets),
                    ("f", f),
                    ("unbiasedMSE", unbiased_mse),
                    ("as.mat", as_mat),
                ),
                lc,
            ),
            lc,
        )
