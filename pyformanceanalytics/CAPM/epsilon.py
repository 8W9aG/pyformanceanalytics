"""The PerformanceAnalytics CAPM epsilon function."""
from typing import Optional

import pandas as pd
from rpy2 import robjects

from ..rimports import ensure_packages_present, PERFORMANCE_ANALYTICS_PACKAGE
from ..xts import xts_from_df


def epsilon(Ra: pd.DataFrame, Rb: pd.DataFrame, Rf: Optional[pd.DataFrame] = None) -> float:
    """Calculate epsilon."""
    ensure_packages_present([PERFORMANCE_ANALYTICS_PACKAGE])
    with robjects.local_context() as lc:
        return robjects.r("CAPM.epsilon").rcall(
            (
                ("Ra", xts_from_df(Ra)),
                ("Rb", xts_from_df(Rb)),
                ("Rf", xts_from_df(Rf) if Rf is not None else 0),
            ),
            lc,
        )[0]
