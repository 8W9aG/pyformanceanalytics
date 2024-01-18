"""The PerformanceAnalytics Return.annualized.excess function."""
from __future__ import annotations

import pandas as pd
from rpy2 import robjects as ro

from ...r_df import as_data_frame
from ...rimports import PERFORMANCE_ANALYTICS_PACKAGE, ensure_packages_present
from ...xts import xts_from_df


def excess(Rp: pd.DataFrame, Rb: pd.DataFrame, geometric: bool = True) -> pd.DataFrame:
    """Calculate Return.annualized.excess."""
    ensure_packages_present([PERFORMANCE_ANALYTICS_PACKAGE])
    with ro.local_context() as lc:
        return as_data_frame(
            ro.r("Return.annualized.excess").rcall(  # type: ignore
                (
                    ("Rp", xts_from_df(Rp)),
                    ("Rb", xts_from_df(Rb)),
                    ("geometric", geometric),
                ),
                lc,
            ),
            lc,
        )
