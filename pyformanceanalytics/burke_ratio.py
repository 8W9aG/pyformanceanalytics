"""The PerformanceAnalytics burke ratio function."""
from typing import Optional

import pandas as pd
from rpy2 import robjects

from .rimports import ensure_packages_present, PERFORMANCE_ANALYTICS_PACKAGE
from .xts import xts_from_df


def burke_ratio(R: pd.DataFrame, Rf: Optional[pd.DataFrame] = None, modified: bool = False) -> float:
    """Calculate BurkeRatio."""
    ensure_packages_present([PERFORMANCE_ANALYTICS_PACKAGE])
    with robjects.local_context() as lc:
        return robjects.r("BurkeRatio").rcall(
            (
                ("R", xts_from_df(R)),
                ("Rf", xts_from_df(Rf) if Rf is not None else 0),
                ("modified", modified),
            ),
            lc,
        )[0]
