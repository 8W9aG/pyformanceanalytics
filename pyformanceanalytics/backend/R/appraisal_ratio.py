"""The PerformanceAnalytics appraisal ratio function."""
from __future__ import annotations

import pandas as pd
from rpy2 import robjects as ro

from .r_df import as_data_frame_or_float
from .rimports import PERFORMANCE_ANALYTICS_PACKAGE, ensure_packages_present
from .xts import xts_from_df


def AppraisalRatio(
    Ra: pd.DataFrame,
    Rb: pd.DataFrame,
    method: str,
    Rf: (pd.DataFrame | float),
) -> pd.DataFrame | float:
    """Calculate AdjustedSharpeRatio."""
    ensure_packages_present([PERFORMANCE_ANALYTICS_PACKAGE])
    with ro.local_context() as lc:
        return as_data_frame_or_float(
            ro.r("AppraisalRatio").rcall(  # type: ignore
                (
                    ("Ra", xts_from_df(Ra)),
                    ("Rb", xts_from_df(Rb)),
                    ("Rf", xts_from_df(Rf) if isinstance(Rf, pd.DataFrame) else Rf),
                    ("method", method),
                ),
                lc,
            ),
            lc,
        )
