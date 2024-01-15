"""The PerformanceAnalytics centeredmoment function."""
from typing import Optional

import pandas as pd
from rpy2 import robjects
from rpy2.robjects import pandas2ri

from .rimports import ensure_packages_present, PERFORMANCE_ANALYTICS_PACKAGE
from .xts import xts_from_df


def centeredmoment(R: pd.DataFrame, power: float = 2.0) -> pd.DataFrame:
    """Calculate centeredmoment."""
    ensure_packages_present([PERFORMANCE_ANALYTICS_PACKAGE])
    with robjects.local_context() as lc:
        with (robjects.default_converter + pandas2ri.converter).context():
            return robjects.conversion.get_conversion().rpy2py(robjects.r("as.data.frame").rcall(
                (
                    ("x", robjects.r("centeredmoment").rcall(
                        (
                            ("R", xts_from_df(R)),
                            ("power", power),
                        ),
                        lc,
                    )),
                ),
                lc,
            ))
