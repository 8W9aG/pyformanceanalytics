"""The PerformanceAnalytics adjusted sharpe ratio function."""
from typing import Optional

import pandas as pd
from rpy2 import robjects

from .rimports import ensure_packages_present, PERFORMANCE_ANALYTICS_PACKAGE
from .xts import xts_from_df


def adjusted_sharpe_ratio(R: pd.DataFrame, Rf: Optional[pd.DataFrame] = None) -> float:
    """Calculate AdjustedSharpeRatio."""
    ensure_packages_present([PERFORMANCE_ANALYTICS_PACKAGE])
    with robjects.local_context() as lc:
        return robjects.r("AdjustedSharpeRatio").rcall(
            (
                ("R", xts_from_df(R)),
                ("Rf", xts_from_df(Rf) if Rf is not None else 0),
            ),
            lc,
        )[0]
