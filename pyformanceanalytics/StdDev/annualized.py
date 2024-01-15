"""The PerformanceAnalytics StdDev.annualized function."""
from typing import Optional

import pandas as pd
from rpy2 import robjects
from rpy2.robjects import pandas2ri

from ..rimports import ensure_packages_present, PERFORMANCE_ANALYTICS_PACKAGE
from ..xts import xts_from_df


def annualized(x: pd.DataFrame) -> pd.DataFrame:
    """Calculate StdDev.annualized."""
    ensure_packages_present([PERFORMANCE_ANALYTICS_PACKAGE])
    with robjects.local_context() as lc:
        with (robjects.default_converter + pandas2ri.converter).context():
            return robjects.conversion.get_conversion().rpy2py(robjects.r("as.data.frame").rcall(
                (
                    ("x", robjects.r("StdDev.annualized").rcall(
                        (
                            ("x", xts_from_df(x)),
                        ),
                        lc,
                    )),
                ),
                lc,
            ))
