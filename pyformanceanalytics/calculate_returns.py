"""The PerformanceAnalytics CalculateReturns function."""
from typing import Optional

import pandas as pd
from rpy2 import robjects
from rpy2.robjects import pandas2ri

from .rimports import ensure_packages_present, PERFORMANCE_ANALYTICS_PACKAGE
from .xts import xts_from_df


def calculate_returns(prices: pd.DataFrame, method: Optional[str] = None) -> pd.DataFrame:
    """Calculate CalculateReturns."""
    if method is None:
        method = "discrete"
    ensure_packages_present([PERFORMANCE_ANALYTICS_PACKAGE])
    with robjects.local_context() as lc:
        with (robjects.default_converter + pandas2ri.converter).context():
            return robjects.conversion.get_conversion().rpy2py(robjects.r("as.data.frame").rcall(
                (
                    ("x", robjects.r("CalculateReturns").rcall(
                        (
                            ("prices", xts_from_df(prices)),
                            ("method", method),
                        ),
                        lc,
                    )),
                ),
                lc,
            ))
