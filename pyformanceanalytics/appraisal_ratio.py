"""The PerformanceAnalytics appraisal ratio function."""
from typing import Optional

import pandas as pd
from rpy2 import robjects

from .rimports import ensure_packages_present, PERFORMANCE_ANALYTICS_PACKAGE
from .xts import xts_from_df


def appraisal_ratio(Ra: pd.DataFrame, Rb: pd.DataFrame, Rf: Optional[pd.DataFrame] = None, method: Optional[str] = None) -> float:
    """Calculate AdjustedSharpeRatio."""
    ensure_packages_present([PERFORMANCE_ANALYTICS_PACKAGE])
    if method is None:
        method = "appraisal"
    with robjects.local_context() as lc:
        return robjects.r("AppraisalRatio").rcall(
            (
                ("Ra", xts_from_df(Ra)),
                ("Rb", xts_from_df(Rb)),
                ("Rf", xts_from_df(Rf) if Rf is not None else 0),
                ("method", method),
            ),
            lc,
        )[0]
