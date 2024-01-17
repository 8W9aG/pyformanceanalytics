"""The PerformanceAnalytics M2.struct function."""
from __future__ import annotations

import pandas as pd
from rpy2 import robjects as ro

from ..r_df import as_data_frame_or_float
from ..rimports import PERFORMANCE_ANALYTICS_PACKAGE, ensure_packages_present
from ..xts import xts_from_df


def struct(
    R: pd.DataFrame, struct_type: (str | None) = None, f: (pd.DataFrame | None) = None
) -> pd.DataFrame | float:
    """Calculate M2.struct."""
    ensure_packages_present([PERFORMANCE_ANALYTICS_PACKAGE])
    if struct_type is None:
        struct_type = "Indep"
    with ro.local_context() as lc:
        return as_data_frame_or_float(
            ro.r("M2.struct").rcall(  # type: ignore
                (
                    ("R", xts_from_df(R)),
                    ("struct", struct_type),
                    ("f", f),
                ),
                lc,
            ),
            lc,
        )
