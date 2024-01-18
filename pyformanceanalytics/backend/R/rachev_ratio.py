"""The PerformanceAnalytics RachevRatio function."""
from __future__ import annotations

import pandas as pd
from rpy2 import robjects as ro

from .r_df import as_data_frame
from .rimports import PERFORMANCE_ANALYTICS_PACKAGE, ensure_packages_present
from .xts import xts_from_df


def RachevRatio(
    R: pd.DataFrame,
    alpha: float = 0.1,
    beta: float = 0.1,
    rf: float = 0.0,
    SE: bool = False,
) -> pd.DataFrame:
    """Calculate RachevRatio."""
    ensure_packages_present([PERFORMANCE_ANALYTICS_PACKAGE])
    with ro.local_context() as lc:
        return as_data_frame(
            ro.r("RachevRatio").rcall(  # type: ignore
                (
                    ("R", xts_from_df(R)),
                    ("alpha", alpha),
                    ("beta", beta),
                    ("rf", rf),
                    ("SE", SE),
                ),
                lc,
            ),
            lc,
        )
