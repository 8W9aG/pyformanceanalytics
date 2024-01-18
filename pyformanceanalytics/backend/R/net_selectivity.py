"""The PerformanceAnalytics NetSelectivity function."""
from __future__ import annotations

import pandas as pd
from rpy2 import robjects as ro

from .r_df import as_data_frame
from .rimports import PERFORMANCE_ANALYTICS_PACKAGE, ensure_packages_present
from .xts import xts_from_df


def NetSelectivity(
    Ra: pd.DataFrame, Rb: pd.DataFrame, Rf: (pd.DataFrame | float)
) -> pd.DataFrame:
    """Calculate NetSelectivity."""
    ensure_packages_present([PERFORMANCE_ANALYTICS_PACKAGE])
    with ro.local_context() as lc:
        return as_data_frame(
            ro.r("NetSelectivity").rcall(  # type: ignore
                (
                    ("Ra", xts_from_df(Ra)),
                    ("Rb", xts_from_df(Rb)),
                    ("Rf", xts_from_df(Rf) if isinstance(Rf, pd.DataFrame) else Rf),
                ),
                lc,
            ),
            lc,
        )
