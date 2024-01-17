"""The PerformanceAnalytics CAPM SML slope function."""
from __future__ import annotations

import pandas as pd
from rpy2 import robjects as ro

from ...r_df import as_data_frame_or_float
from ...rimports import PERFORMANCE_ANALYTICS_PACKAGE, ensure_packages_present
from ...xts import xts_from_df


def slope(Rb: pd.DataFrame, Rf: (pd.DataFrame | None) = None) -> pd.DataFrame | float:
    """Calculate slope."""
    ensure_packages_present([PERFORMANCE_ANALYTICS_PACKAGE])
    with ro.local_context() as lc:
        return as_data_frame_or_float(
            ro.r("CAPM.SML.slope").rcall(  # type: ignore
                (
                    ("Rb", xts_from_df(Rb)),
                    ("Rf", xts_from_df(Rf) if Rf is not None else 0),
                ),
                lc,
            ),
            lc,
        )
