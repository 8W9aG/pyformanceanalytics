"""The PerformanceAnalytics table.Variability function."""
import pandas as pd
from rpy2 import robjects as ro

from ..r_df import as_data_frame
from ..rimports import PERFORMANCE_ANALYTICS_PACKAGE, ensure_packages_present
from ..xts import xts_from_df


def Variability(
    R: pd.DataFrame, geometric: bool = True, digits: int = 4
) -> pd.DataFrame:
    """Calculate table.Variability."""
    ensure_packages_present([PERFORMANCE_ANALYTICS_PACKAGE])
    with ro.local_context() as lc:
        return as_data_frame(
            ro.r("table.Variability").rcall(  # type: ignore
                (
                    ("R", xts_from_df(R)),
                    ("geometric", geometric),
                    ("digits", digits),
                ),
                lc,
            ),
            lc,
        )
