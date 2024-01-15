"""The PerformanceAnalytics Return.clean function."""
from typing import Optional

import pandas as pd
from rpy2 import robjects
from rpy2.robjects import pandas2ri

from ..rimports import ensure_packages_present, PERFORMANCE_ANALYTICS_PACKAGE
from ..xts import xts_from_df


def clean(R: pd.DataFrame, method: Optional[str] = None, alpha = 0.01) -> pd.DataFrame:
    """Calculate Return.clean."""
    ensure_packages_present([PERFORMANCE_ANALYTICS_PACKAGE])
    if method is None:
        method = "none"
    with robjects.local_context() as lc:
        with (robjects.default_converter + pandas2ri.converter).context():
            return robjects.conversion.get_conversion().rpy2py(robjects.r("as.data.frame").rcall(
                (
                    ("x", robjects.r("Return.clean").rcall(
                        (
                            ("R", xts_from_df(R)),
                            ("method", method),
                            ("alpha", alpha),
                        ),
                        lc,
                    )),
                ),
                lc,
            ))
