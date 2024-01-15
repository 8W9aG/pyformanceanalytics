"""The PerformanceAnalytics Return.locScaleRob function."""
from typing import Optional

import pandas as pd
from rpy2 import robjects
from rpy2.robjects import pandas2ri

from ..rimports import ensure_packages_present, PERFORMANCE_ANALYTICS_PACKAGE, PKG_PACKAGE
from ..xts import xts_from_df


def loc_scale_rob(R: pd.DataFrame, alpha_robust: float = 0.05, normal_efficiency: float = 0.99) -> pd.DataFrame:
    """Calculate Return.locScaleRob."""
    ensure_packages_present([PERFORMANCE_ANALYTICS_PACKAGE, PKG_PACKAGE])
    with robjects.local_context() as lc:
        with (robjects.default_converter + pandas2ri.converter).context():
            return robjects.conversion.get_conversion().rpy2py(robjects.r("as.data.frame").rcall(
                (
                    ("x", robjects.r("Return.locScaleRob").rcall(
                        (
                            ("R", xts_from_df(R)),
                            ("alpha.robust", alpha_robust),
                            ("normal.efficiency", normal_efficiency),
                        ),
                        lc,
                    )),
                ),
                lc,
            ))
