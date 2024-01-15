"""The PerformanceAnalytics maxDrawdown function."""
from typing import Optional, List

import pandas as pd
from rpy2 import robjects
from rpy2.robjects import pandas2ri

from .rimports import ensure_packages_present, PERFORMANCE_ANALYTICS_PACKAGE
from .xts import xts_from_df


def max_drawdown(R: pd.DataFrame, weights: Optional[List[float]] = None, geometric: bool = True, invert: bool = True) -> pd.DataFrame:
    """Calculate maxDrawdown."""
    ensure_packages_present([PERFORMANCE_ANALYTICS_PACKAGE])
    with robjects.local_context() as lc:
        with (robjects.default_converter + pandas2ri.converter).context():
            return robjects.conversion.get_conversion().rpy2py(robjects.r("as.data.frame").rcall(
                (
                    ("x", robjects.r("maxDrawdown").rcall(
                        (
                            ("R", xts_from_df(R)),
                            ("weights", weights),
                            ("geometric", geometric),
                            ("invert", invert),
                        ),
                        lc,
                    )),
                ),
                lc,
            ))
