"""The PerformanceAnalytics SortinoRatio function."""
from typing import Optional

import pandas as pd
from rpy2 import robjects
from rpy2.robjects import pandas2ri

from .rimports import ensure_packages_present, PERFORMANCE_ANALYTICS_PACKAGE
from .xts import xts_from_df


def sortino_ratio(R: pd.DataFrame, MAR: float = 0.0, weights: Optional[pd.DataFrame] = None, threshold: Optional[str] = None, SE: bool = False) -> pd.DataFrame:
    """Calculate SortinoRatio."""
    ensure_packages_present([PERFORMANCE_ANALYTICS_PACKAGE])
    if threshold is None:
        threshold = "MAR"
    with robjects.local_context() as lc:
        with (robjects.default_converter + pandas2ri.converter).context():
            return robjects.conversion.get_conversion().rpy2py(robjects.r("as.data.frame").rcall(
                (
                    ("x", robjects.r("SortinoRatio").rcall(
                        (
                            ("R", xts_from_df(R)),
                            ("MAR", MAR),
                            ("weights", weights),
                            ("threshold", threshold),
                            ("SE", SE),
                        ),
                        lc,
                    )),
                ),
                lc,
            ))
