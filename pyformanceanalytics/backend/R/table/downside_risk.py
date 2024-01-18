"""The PerformanceAnalytics table.DownsideRisk function."""
from __future__ import annotations

import pandas as pd
from rpy2 import robjects as ro

from ..r_df import as_data_frame
from ..rimports import PERFORMANCE_ANALYTICS_PACKAGE, ensure_packages_present
from ..xts import xts_from_df


def DownsideRisk(
    R: pd.DataFrame,
    ci: float = 0.95,
    Rf: (pd.DataFrame | None) = None,
    MAR: float = 0.1 / 12.0,
    p: float = 0.95,
    digits: int = 4,
) -> pd.DataFrame:
    """Calculate table.DownsideRisk."""
    ensure_packages_present([PERFORMANCE_ANALYTICS_PACKAGE])
    with ro.local_context() as lc:
        return as_data_frame(
            ro.r("table.DownsideRisk").rcall(  # type: ignore
                (
                    ("R", xts_from_df(R)),
                    ("ci", ci),
                    ("Rf", 0 if Rf is None else xts_from_df(Rf)),
                    ("MAR", MAR),
                    ("p", p),
                    ("digits", digits),
                ),
                lc,
            ),
            lc,
        )
