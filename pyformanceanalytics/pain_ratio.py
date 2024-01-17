"""The PerformanceAnalytics PainRatio function."""
from __future__ import annotations

import pandas as pd
from rpy2 import robjects as ro

from .r_df import as_data_frame_or_float
from .rimports import PERFORMANCE_ANALYTICS_PACKAGE, ensure_packages_present
from .xts import xts_from_df


def PainRatio(
    R: pd.DataFrame, Rf: (pd.DataFrame | None) = None
) -> pd.DataFrame | float:
    """Calculate PainRatio."""
    ensure_packages_present([PERFORMANCE_ANALYTICS_PACKAGE])
    with ro.local_context() as lc:
        return as_data_frame_or_float(
            ro.r("PainRatio").rcall(  # type: ignore
                (
                    ("R", xts_from_df(R)),
                    ("Rf", 0 if Rf is None else xts_from_df(Rf)),
                ),
                lc,
            ),
            lc,
        )
