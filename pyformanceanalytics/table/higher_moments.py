"""The PerformanceAnalytics table.HigherMoments function."""
from typing import Optional

import pandas as pd
from rpy2 import robjects
from rpy2.robjects import pandas2ri

from ..rimports import ensure_packages_present, PERFORMANCE_ANALYTICS_PACKAGE
from ..xts import xts_from_df


def higher_moments(Ra: pd.DataFrame, Rb: pd.DataFrame, Rf: Optional[pd.DataFrame] = None, digits: int = 4, method: Optional[str] = None) -> pd.DataFrame:
    """Calculate table.HigherMoments."""
    ensure_packages_present([PERFORMANCE_ANALYTICS_PACKAGE])
    if method is None:
        method = "moment"
    with robjects.local_context() as lc:
        with (robjects.default_converter + pandas2ri.converter).context():
            return robjects.conversion.get_conversion().rpy2py(robjects.r("as.data.frame").rcall(
                (
                    ("x", robjects.r("table.HigherMoments").rcall(
                        (
                            ("Ra", xts_from_df(Ra)),
                            ("Rb", xts_from_df(Rb)),
                            ("Rf", 0 if Rf is None else xts_from_df(Rf)),
                            ("digits", digits),
                            ("method", method),
                        ),
                        lc,
                    )),
                ),
                lc,
            ))
