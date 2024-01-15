"""The PerformanceAnalytics CAPM dynamic function."""
from typing import Optional

import pandas as pd
from rpy2 import robjects

from ..rimports import ensure_packages_present, PERFORMANCE_ANALYTICS_PACKAGE
from ..xts import xts_from_df


def dynamic(Ra: pd.DataFrame, Rb: pd.DataFrame, Z: pd.DataFrame, Rf: Optional[pd.DataFrame] = None, lags: int = 1) -> float:
    """Calculate dynamic."""
    ensure_packages_present([PERFORMANCE_ANALYTICS_PACKAGE])
    with robjects.local_context() as lc:
        return robjects.r("CAPM.dynamic").rcall(
            (
                ("Ra", xts_from_df(Ra)),
                ("Rb", xts_from_df(Rb)),
                ("Z", xts_from_df(Z)),
                ("Rf", xts_from_df(Rf) if Rf is not None else 0),
                ("lags", lags),
            ),
            lc,
        )[0]
