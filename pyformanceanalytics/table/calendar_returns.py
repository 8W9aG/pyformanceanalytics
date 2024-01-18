"""The PerformanceAnalytics table.CalendarReturns function."""
import pandas as pd
from rpy2 import robjects as ro

from ..r_df import as_data_frame
from ..rimports import PERFORMANCE_ANALYTICS_PACKAGE, ensure_packages_present
from ..xts import xts_from_df


def CalendarReturns(
    R: pd.DataFrame, digits: int = 1, as_perc: bool = True, geometric: bool = True
) -> pd.DataFrame:
    """Calculate table.CalendarReturns."""
    ensure_packages_present([PERFORMANCE_ANALYTICS_PACKAGE])
    with ro.local_context() as lc:
        return as_data_frame(
            ro.r("table.CalendarReturns").rcall(  # type: ignore
                (
                    ("R", xts_from_df(R)),
                    ("digits", digits),
                    ("as.perc", as_perc),
                    ("geometric", geometric),
                ),
                lc,
            ),
            lc,
        )
