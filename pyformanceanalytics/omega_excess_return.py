"""The PerformanceAnalytics OmegaExcessReturn function."""
from __future__ import annotations

import pandas as pd
from rpy2 import robjects as ro

from .r_df import as_data_frame_or_float
from .rimports import PERFORMANCE_ANALYTICS_PACKAGE, ensure_packages_present
from .xts import xts_from_df


def OmegaExcessReturn(
    Ra: pd.DataFrame, Rb: pd.DataFrame, MAR: float = 0.0
) -> pd.DataFrame | float:
    """Calculate OmegaExcessReturn."""
    ensure_packages_present([PERFORMANCE_ANALYTICS_PACKAGE])
    with ro.local_context() as lc:
        return as_data_frame_or_float(
            ro.r("OmegaExcessReturn").rcall(  # type: ignore
                (
                    ("Ra", xts_from_df(Ra)),
                    ("Rb", xts_from_df(Rb)),
                    ("MAR", MAR),
                ),
                lc,
            ),
            lc,
        )
