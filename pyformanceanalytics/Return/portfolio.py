"""The PerformanceAnalytics Return.portfolio function."""
from __future__ import annotations

import pandas as pd
from rpy2 import robjects as ro

from ..r_df import as_data_frame_or_float
from ..rimports import (PERFORMANCE_ANALYTICS_PACKAGE, PKG_PACKAGE,
                        ensure_packages_present)
from ..xts import xts_from_df


def portfolio(
    R: pd.DataFrame,
    weights: (pd.DataFrame | None) = None,
    wealth_index: bool = False,
    contribution: bool = False,
    geometric: bool = True,
    rebalance_on: (str | None) = None,
    value: int = 1,
    verbose: bool = False,
) -> pd.DataFrame | float:
    """Calculate Return.portfolio."""
    ensure_packages_present([PERFORMANCE_ANALYTICS_PACKAGE, PKG_PACKAGE])
    with ro.local_context() as lc:
        return as_data_frame_or_float(
            ro.r("Return.portfolio").rcall(  # type: ignore
                (
                    ("R", xts_from_df(R)),
                    ("weights", weights),
                    ("wealth.index", wealth_index),
                    ("contribution", contribution),
                    ("geometric", geometric),
                    ("rebalance_on", rebalance_on),
                    ("value", value),
                    ("verbose", verbose),
                ),
                lc,
            ),
            lc,
        )
