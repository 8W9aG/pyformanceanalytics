"""The PerformanceAnalytics UpDownRatios function."""
from typing import Optional

import pandas as pd
from rpy2 import robjects
from rpy2.robjects import pandas2ri

from .rimports import ensure_packages_present, PERFORMANCE_ANALYTICS_PACKAGE
from .xts import xts_from_df


def up_down_ratios(Ra: pd.DataFrame, Rb: pd.DataFrame, method: Optional[str] = None, side: Optional[str] = None) -> pd.DataFrame:
    """Calculate UpDownRatios."""
    ensure_packages_present([PERFORMANCE_ANALYTICS_PACKAGE])
    if method is None:
        method = "Capture"
    if side is None:
        side = "Up"
    with robjects.local_context() as lc:
        with (robjects.default_converter + pandas2ri.converter).context():
            return robjects.conversion.get_conversion().rpy2py(robjects.r("as.data.frame").rcall(
                (
                    ("x", robjects.r("UpDownRatios").rcall(
                        (
                            ("Ra", xts_from_df(Ra)),
                            ("Rb", xts_from_df(Rb)),
                            ("method", method),
                            ("side", side),
                        ),
                        lc,
                    )),
                ),
                lc,
            ))
