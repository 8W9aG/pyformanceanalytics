"""The PerformanceAnalytics RPESE.control function."""
from __future__ import annotations

import pandas as pd
from rpy2 import robjects as ro

from ..r_df import as_data_frame
from ..rimports import PERFORMANCE_ANALYTICS_PACKAGE, ensure_packages_present


def control(
    estimator: str,
    se_method: (str | None) = None,
    clean_outliers: (bool | None) = None,
    fitting_method: (str | None) = None,
    freq_include: (str | None) = None,
    freq_par: (float | None) = None,
    a: (float | None) = None,
    b: (float | None) = None,
) -> pd.DataFrame:
    """Calculate RPESE.control."""
    ensure_packages_present([PERFORMANCE_ANALYTICS_PACKAGE])
    with ro.local_context() as lc:
        return as_data_frame(
            ro.r("RPESE.control").rcall(  # type: ignore
                (
                    ("estimator", estimator),
                    ("se.method", se_method),
                    ("cleanOutliers", clean_outliers),
                    ("fitting.method", fitting_method),
                    ("freq.include", freq_include),
                    ("freq.par", freq_par),
                    ("a", a),
                    ("b", b),
                ),
                lc,
            ),
            lc,
        )
