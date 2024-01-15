"""The PerformanceAnalytics SharpeRatio.modified function."""
from typing import Optional

import pandas as pd
from rpy2 import robjects
from rpy2.robjects import pandas2ri

from ..rimports import ensure_packages_present, PERFORMANCE_ANALYTICS_PACKAGE
from ..xts import xts_from_df


def modified(R: pd.DataFrame, Rf: Optional[pd.DataFrame] = None, p: float = 0.95, FUN: Optional[str] = None, weights: Optional[pd.DataFrame] = None) -> pd.DataFrame:
    """Calculate SharpeRatio.modified."""
    ensure_packages_present([PERFORMANCE_ANALYTICS_PACKAGE])
    if FUN is None:
        FUN = "StdDev"
    with robjects.local_context() as lc:
        with (robjects.default_converter + pandas2ri.converter).context():
            return robjects.conversion.get_conversion().rpy2py(robjects.r("as.data.frame").rcall(
                (
                    ("x", robjects.r("SharpeRatio.modified").rcall(
                        (
                            ("R", xts_from_df(R)),
                            ("Rf", 0 if Rf is None else xts_from_df(Rf)),
                            ("p", p),
                            ("FUN", FUN),
                            ("weights", weights),
                        ),
                        lc,
                    )),
                ),
                lc,
            ))