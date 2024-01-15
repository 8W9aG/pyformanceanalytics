"""The PerformanceAnalytics table.Autocorrelation function."""
import pandas as pd
from rpy2 import robjects
from rpy2.robjects import pandas2ri

from ..rimports import ensure_packages_present, PERFORMANCE_ANALYTICS_PACKAGE
from ..xts import xts_from_df


def autocorrelation(R: pd.DataFrame, digits: int = 4) -> pd.DataFrame:
    """Calculate table.Autocorrelation."""
    ensure_packages_present([PERFORMANCE_ANALYTICS_PACKAGE])
    with robjects.local_context() as lc:
        with (robjects.default_converter + pandas2ri.converter).context():
            return robjects.conversion.get_conversion().rpy2py(robjects.r("as.data.frame").rcall(
                (
                    ("x", robjects.r("table.Autocorrelation").rcall(
                        (
                            ("R", xts_from_df(R)),
                            ("digits", digits),
                        ),
                        lc,
                    )),
                ),
                lc,
            ))
