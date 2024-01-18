"""The PerformanceAnalytics findDrawdowns function."""
import pandas as pd
from rpy2 import robjects as ro

from .r_df import as_data_frame
from .rimports import PERFORMANCE_ANALYTICS_PACKAGE, ensure_packages_present
from .xts import xts_from_df


def findDrawdowns(R: pd.DataFrame, geometric: bool = True) -> pd.DataFrame:
    """Calculate findDrawdowns."""
    ensure_packages_present([PERFORMANCE_ANALYTICS_PACKAGE])
    with ro.local_context() as lc:
        return as_data_frame(
            ro.r("findDrawdowns").rcall(  # type: ignore
                (
                    ("R", xts_from_df(R)),
                    ("geometric", geometric),
                ),
                lc,
            ),
            lc,
        )
