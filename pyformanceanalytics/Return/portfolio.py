"""The PerformanceAnalytics Return.portfolio function."""
from typing import Optional

import pandas as pd
from rpy2 import robjects
from rpy2.robjects import pandas2ri

from ..rimports import ensure_packages_present, PERFORMANCE_ANALYTICS_PACKAGE, PKG_PACKAGE
from ..xts import xts_from_df


def portfolio(R: pd.DataFrame, weights: Optional[pd.DataFrame] = None, wealth_index: bool = False, contribution: bool = False, geometric: bool = True, rebalance_on: Optional[str] = None, value: int = 1, verbose: bool = False) -> pd.DataFrame:
    """Calculate Return.portfolio."""
    ensure_packages_present([PERFORMANCE_ANALYTICS_PACKAGE, PKG_PACKAGE])
    with robjects.local_context() as lc:
        with (robjects.default_converter + pandas2ri.converter).context():
            return robjects.conversion.get_conversion().rpy2py(robjects.r("as.data.frame").rcall(
                (
                    ("x", robjects.r("Return.portfolio").rcall(
                        (
                            ("R", xts_from_df(R)),
                            ("weights", weights),
                            ("wealth.index", wealth_index),
                            ("contribution", contribution),
                            ("geometric", geometric),
                            ("rebalance_on", rebalance_on),
                            ("value", value),
                            ("verbose", verbose),
                        ),
                        lc,
                    )),
                ),
                lc,
            ))
