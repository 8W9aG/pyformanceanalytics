"""The PerformanceAnalytics Return.convert function."""
from __future__ import annotations

import pandas as pd
from rpy2 import robjects as ro

from ..r_df import as_data_frame_or_float
from ..rimports import PERFORMANCE_ANALYTICS_PACKAGE, ensure_packages_present
from ..xts import xts_from_df


def convert(
    R: pd.DataFrame,
    destination_type: str,
    seed_value: (float | None) = None,
    initial: bool = True,
) -> pd.DataFrame | float:
    """Calculate Return.convert."""
    ensure_packages_present([PERFORMANCE_ANALYTICS_PACKAGE])
    with ro.local_context() as lc:
        return as_data_frame_or_float(
            ro.r("Return.convert").rcall(  # type: ignore
                (
                    ("R", xts_from_df(R)),
                    ("destinationType", destination_type),
                    ("seedValue", seed_value),
                    ("initial", initial),
                ),
                lc,
            ),
            lc,
        )
