"""The PerformanceAnalytics table.DrawdownsRatio function."""
from typing import Optional

import pandas as pd
from rpy2 import robjects
from rpy2.robjects import pandas2ri

from ..rimports import ensure_packages_present, PERFORMANCE_ANALYTICS_PACKAGE
from ..xts import xts_from_df


def drawdowns_ratio(R: pd.DataFrame, Rf: Optional[pd.DataFrame] = None, digits: int = 4) -> pd.DataFrame:
    """Calculate table.DrawdownsRatio."""
    ensure_packages_present([PERFORMANCE_ANALYTICS_PACKAGE])
    with robjects.local_context() as lc:
        with (robjects.default_converter + pandas2ri.converter).context():
            return robjects.conversion.get_conversion().rpy2py(robjects.r("as.data.frame").rcall(
                (
                    ("x", robjects.r("table.DrawdownsRatio").rcall(
                        (
                            ("R", xts_from_df(R)),
                            ("Rf", 0 if Rf is None else xts_from_df(Rf)),
                            ("digits", digits),
                        ),
                        lc,
                    )),
                ),
                lc,
            ))
