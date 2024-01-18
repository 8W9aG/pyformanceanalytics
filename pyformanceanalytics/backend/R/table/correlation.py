"""The PerformanceAnalytics table.Correlation function."""
import pandas as pd
from rpy2 import robjects as ro

from ..r_df import as_data_frame
from ..rimports import PERFORMANCE_ANALYTICS_PACKAGE, ensure_packages_present
from ..xts import xts_from_df


def Correlation(Ra: pd.DataFrame, Rb: pd.DataFrame) -> pd.DataFrame:
    """Calculate table.Correlation."""
    ensure_packages_present([PERFORMANCE_ANALYTICS_PACKAGE])
    with ro.local_context() as lc:
        return as_data_frame(
            ro.r("table.Correlation").rcall(  # type: ignore
                (
                    ("Ra", xts_from_df(Ra)),
                    ("Rb", xts_from_df(Rb)),
                ),
                lc,
            ),
            lc,
        )
