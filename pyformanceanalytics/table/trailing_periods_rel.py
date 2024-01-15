"""The PerformanceAnalytics table.TrailingPeriodsRel function."""
from typing import Optional, List

import pandas as pd
from rpy2 import robjects
from rpy2.robjects import pandas2ri
from rpy2.robjects.vectors import IntVector, StrVector

from ..rimports import ensure_packages_present, PERFORMANCE_ANALYTICS_PACKAGE
from ..xts import xts_from_df


def trailing_periods_rel(R: pd.DataFrame, Rb: pd.DataFrame, periods: Optional[List[int]] = None, funcs_names: Optional[List[str]] = None, digits: int = 4) -> pd.DataFrame:
    """Calculate table.TrailingPeriodsRel."""
    ensure_packages_present([PERFORMANCE_ANALYTICS_PACKAGE])
    if periods is None:
        periods = [12, 36, 60]
    if funcs_names is None:
        funcs_names = ["Correlation", "Beta"]
    with robjects.local_context() as lc:
        with (robjects.default_converter + pandas2ri.converter).context():
            return robjects.conversion.get_conversion().rpy2py(robjects.r("as.data.frame").rcall(
                (
                    ("x", robjects.r("table.TrailingPeriodsRel").rcall(
                        (
                            ("R", xts_from_df(R)),
                            ("Rb", xts_from_df(Rb)),
                            ("periods", IntVector(periods)),
                            ("funcs.names", StrVector(funcs_names)),
                            ("digits", digits),
                        ),
                        lc,
                    )),
                ),
                lc,
            ))
