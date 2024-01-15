"""The PerformanceAnalytics table.Drawdowns function."""
import pandas as pd
from rpy2 import robjects
from rpy2.robjects import pandas2ri

from ..rimports import ensure_packages_present, PERFORMANCE_ANALYTICS_PACKAGE
from ..xts import xts_from_df


def drawdowns(R: pd.DataFrame, top: int = 5, digits: int = 4, geometric: bool = True) -> pd.DataFrame:
    """Calculate table.Drawdowns."""
    ensure_packages_present([PERFORMANCE_ANALYTICS_PACKAGE])
    with robjects.local_context() as lc:
        with (robjects.default_converter + pandas2ri.converter).context():
            return robjects.conversion.get_conversion().rpy2py(robjects.r("as.data.frame").rcall(
                (
                    ("x", robjects.r("table.Drawdowns").rcall(
                        (
                            ("R", xts_from_df(R)),
                            ("top", top),
                            ("digits", digits),
                            ("geometric", geometric),
                        ),
                        lc,
                    )),
                ),
                lc,
            ))
