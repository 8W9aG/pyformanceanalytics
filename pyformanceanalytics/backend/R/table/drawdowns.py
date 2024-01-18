"""The PerformanceAnalytics table.Drawdowns function."""
import pandas as pd
from rpy2 import robjects as ro

from ..r_df import as_data_frame
from ..rimports import PERFORMANCE_ANALYTICS_PACKAGE, ensure_packages_present
from ..xts import xts_from_df


def Drawdowns(
    R: pd.DataFrame, top: int = 5, digits: int = 4, geometric: bool = True
) -> pd.DataFrame:
    """Calculate table.Drawdowns."""
    ensure_packages_present([PERFORMANCE_ANALYTICS_PACKAGE])
    with ro.local_context() as lc:
        return as_data_frame(
            ro.r("table.Drawdowns").rcall(  # type: ignore
                (
                    ("R", xts_from_df(R)),
                    ("top", top),
                    ("digits", digits),
                    ("geometric", geometric),
                ),
                lc,
            ),
            lc,
        )
