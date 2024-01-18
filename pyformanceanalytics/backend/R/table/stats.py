"""The PerformanceAnalytics table.Stats function."""
import pandas as pd
from rpy2 import robjects as ro

from ..r_df import as_data_frame
from ..rimports import PERFORMANCE_ANALYTICS_PACKAGE, ensure_packages_present
from ..xts import xts_from_df


def Stats(R: pd.DataFrame, ci: float = 0.95, digits: int = 4) -> pd.DataFrame:
    """Calculate table.Stats."""
    ensure_packages_present([PERFORMANCE_ANALYTICS_PACKAGE])
    with ro.local_context() as lc:
        return as_data_frame(
            ro.r("table.Stats").rcall(  # type: ignore
                (
                    ("R", xts_from_df(R)),
                    ("ci", ci),
                    ("digits", digits),
                ),
                lc,
            ),
            lc,
        )
