"""The PerformanceAnalytics CAPM CML slope function."""
from typing import Optional

import pandas as pd
from rpy2 import robjects

from ...rimports import ensure_packages_present, PERFORMANCE_ANALYTICS_PACKAGE
from ...xts import xts_from_df


def slope(Rb: pd.DataFrame, Rf: Optional[pd.DataFrame] = None) -> float:
    """Calculate slope."""
    ensure_packages_present([PERFORMANCE_ANALYTICS_PACKAGE])
    with robjects.local_context() as lc:
        return robjects.r("CAPM.CML.slope").rcall(
            (
                ("Rb", xts_from_df(Rb)),
                ("Rf", xts_from_df(Rf) if Rf is not None else 0),
            ),
            lc,
        )[0]
