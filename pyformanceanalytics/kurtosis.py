"""The PerformanceAnalytics kurtosis function."""
from typing import Optional

import pandas as pd
from rpy2 import robjects
from rpy2.robjects import pandas2ri

from .rimports import ensure_packages_present, PERFORMANCE_ANALYTICS_PACKAGE
from .xts import xts_from_df


def kurtosis(x: pd.DataFrame, na_rm: bool = False, method: Optional[str] = None) -> pd.DataFrame:
    """Calculate kurtosis."""
    ensure_packages_present([PERFORMANCE_ANALYTICS_PACKAGE])
    if method is None:
        method = "moment"
    with robjects.local_context() as lc:
        with (robjects.default_converter + pandas2ri.converter).context():
            return robjects.conversion.get_conversion().rpy2py(robjects.r("as.data.frame").rcall(
                (
                    ("x", robjects.r("kurtosis").rcall(
                        (
                            ("x", xts_from_df(x)),
                            ("na.rm", na_rm),
                            ("method", method),
                        ),
                        lc,
                    )),
                ),
                lc,
            ))
