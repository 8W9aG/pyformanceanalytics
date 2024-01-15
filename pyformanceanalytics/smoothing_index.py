"""The PerformanceAnalytics SmoothingIndex function."""
import pandas as pd
from rpy2 import robjects
from rpy2.robjects import pandas2ri

from .rimports import ensure_packages_present, PERFORMANCE_ANALYTICS_PACKAGE
from .xts import xts_from_df


def smoothing_index(R: pd.DataFrame, neg_thetas: bool = False, ma_order: int = 2, verbose: bool = False) -> pd.DataFrame:
    """Calculate SmoothingIndex."""
    ensure_packages_present([PERFORMANCE_ANALYTICS_PACKAGE])
    with robjects.local_context() as lc:
        with (robjects.default_converter + pandas2ri.converter).context():
            return robjects.conversion.get_conversion().rpy2py(robjects.r("as.data.frame").rcall(
                (
                    ("x", robjects.r("SmoothingIndex").rcall(
                        (
                            ("R", xts_from_df(R)),
                            ("neg.thetas", neg_thetas),
                            ("MAorder", ma_order),
                            ("verbose", verbose),
                        ),
                        lc,
                    )),
                ),
                lc,
            ))
