"""The PerformanceAnalytics Kappa function."""
# ruff: noqa: E741
from __future__ import annotations

import pandas as pd
from rpy2 import robjects as ro

from .r_df import as_data_frame_or_float
from .rimports import PERFORMANCE_ANALYTICS_PACKAGE, ensure_packages_present
from .xts import xts_from_df


def Kappa(R: pd.DataFrame, MAR: float = 0.005, l: int = 2) -> pd.DataFrame | float:  # noqa: E741
    """Calculate Kappa."""
    ensure_packages_present([PERFORMANCE_ANALYTICS_PACKAGE])
    with ro.local_context() as lc:
        return as_data_frame_or_float(
            ro.r("Kappa").rcall(  # type: ignore
                (
                    ("R", xts_from_df(R)),
                    ("MAR", MAR),
                    ("l", l),
                ),
                lc,
            ),
            lc,
        )
