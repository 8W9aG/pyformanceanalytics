"""The PerformanceAnalytics table.ProbOutPerformance function."""
from typing import Optional, List

import pandas as pd
from rpy2 import robjects
from rpy2.robjects import pandas2ri
from rpy2.robjects.vectors import IntVector

from ..rimports import ensure_packages_present, PERFORMANCE_ANALYTICS_PACKAGE
from ..xts import xts_from_df


def prob_out_performance(R: pd.DataFrame, Rb: pd.DataFrame, period_lengths: Optional[List[int]] = None) -> pd.DataFrame:
    """Calculate table.ProbOutPerformance."""
    ensure_packages_present([PERFORMANCE_ANALYTICS_PACKAGE])
    if period_lengths is None:
        period_lengths = [1, 3, 6, 9, 12, 18, 36]
    with robjects.local_context() as lc:
        with (robjects.default_converter + pandas2ri.converter).context():
            return robjects.conversion.get_conversion().rpy2py(robjects.r("as.data.frame").rcall(
                (
                    ("x", robjects.r("table.ProbOutPerformance").rcall(
                        (
                            ("R", xts_from_df(R)),
                            ("Rb", xts_from_df(Rb)),
                            ("period_lengths", IntVector(period_lengths)),
                        ),
                        lc,
                    )),
                ),
                lc,
            ))
