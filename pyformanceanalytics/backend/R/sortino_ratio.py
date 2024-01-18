"""The PerformanceAnalytics SortinoRatio function."""
from __future__ import annotations

import pandas as pd
from rpy2 import robjects as ro

from .r_df import as_data_frame
from .rimports import PERFORMANCE_ANALYTICS_PACKAGE, ensure_packages_present
from .xts import xts_from_df


def SortinoRatio(
    R: pd.DataFrame,
    threshold: str,
    MAR: float = 0.0,
    weights: (pd.DataFrame | None) = None,
    SE: bool = False,
) -> pd.DataFrame:
    """Calculate SortinoRatio."""
    ensure_packages_present([PERFORMANCE_ANALYTICS_PACKAGE])
    with ro.local_context() as lc:
        return as_data_frame(
            ro.r("SortinoRatio").rcall(  # type: ignore
                (
                    ("R", xts_from_df(R)),
                    ("MAR", MAR),
                    ("weights", weights),
                    ("threshold", threshold),
                    ("SE", SE),
                ),
                lc,
            ),
            lc,
        )
