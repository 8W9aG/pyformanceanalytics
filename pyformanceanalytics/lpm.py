"""The PerformanceAnalytics lpm function."""
from typing import Optional

import pandas as pd
from rpy2 import robjects
from rpy2.robjects import pandas2ri

from .rimports import ensure_packages_present, PERFORMANCE_ANALYTICS_PACKAGE
from .xts import xts_from_df


def lpm(R: pd.DataFrame, n: int = 2, threshold: int = 0, about_mean: bool = False, SE: bool = False) -> pd.DataFrame:
    """Calculate lpm."""
    ensure_packages_present([PERFORMANCE_ANALYTICS_PACKAGE])
    with robjects.local_context() as lc:
        with (robjects.default_converter + pandas2ri.converter).context():
            return robjects.conversion.get_conversion().rpy2py(robjects.r("as.data.frame").rcall(
                (
                    ("x", robjects.r("lpm").rcall(
                        (
                            ("R", xts_from_df(R)),
                            ("n", n),
                            ("threshold", threshold),
                            ("about.mean", about_mean),
                            ("SE", SE),
                        ),
                        lc,
                    )),
                ),
                lc,
            ))
