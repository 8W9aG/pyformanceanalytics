"""The PerformanceAnalytics centeredcomoment function."""
from __future__ import annotations

import pandas as pd
from rpy2 import robjects as ro

from .r_df import as_data_frame_or_float
from .rimports import PERFORMANCE_ANALYTICS_PACKAGE, ensure_packages_present
from .xts import xts_from_df


def centeredcomoment(
    Ra: pd.DataFrame, Rb: pd.DataFrame, p1: float, p2: float, normalize: bool = False
) -> pd.DataFrame | float:
    """Calculate centeredcomoment."""
    ensure_packages_present([PERFORMANCE_ANALYTICS_PACKAGE])
    with ro.local_context() as lc:
        return as_data_frame_or_float(
            ro.r("centeredcomoment").rcall(  # type: ignore
                (
                    ("Ra", xts_from_df(Ra)),
                    ("Rb", xts_from_df(Rb)),
                    ("p1", p1),
                    ("p2", p2),
                    ("normalize", normalize),
                ),
                lc,
            ),
            lc,
        )
