"""The PerformanceAnalytics sortDrawdowns function."""
import pandas as pd
from rpy2 import robjects as ro

from .r_df import as_data_frame
from .rimports import PERFORMANCE_ANALYTICS_PACKAGE, ensure_packages_present


def sort_drawdowns(runs: pd.DataFrame) -> pd.DataFrame:
    """Calculate sortDrawdowns."""
    ensure_packages_present([PERFORMANCE_ANALYTICS_PACKAGE])
    with ro.local_context() as lc:
        return as_data_frame(
            ro.r("sortDrawdowns").rcall(  # type: ignore
                (("runs", runs),),
                lc,
            ),
            lc,
        )
