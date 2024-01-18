"""The PerformanceAnalytics table.DrawdownsRatio function."""
from __future__ import annotations

import pandas as pd
from rpy2 import robjects as ro

from ..r_df import as_data_frame
from ..rimports import PERFORMANCE_ANALYTICS_PACKAGE, ensure_packages_present
from ..xts import xts_from_df


def DrawdownsRatio(
    R: pd.DataFrame, Rf: (pd.DataFrame | float), digits: int = 4
) -> pd.DataFrame:
    """Calculate table.DrawdownsRatio."""
    ensure_packages_present([PERFORMANCE_ANALYTICS_PACKAGE])
    with ro.local_context() as lc:
        return as_data_frame(
            ro.r("table.DrawdownsRatio").rcall(  # type: ignore
                (
                    ("R", xts_from_df(R)),
                    ("Rf", xts_from_df(Rf) if isinstance(Rf, pd.DataFrame) else Rf),
                    ("digits", digits),
                ),
                lc,
            ),
            lc,
        )
