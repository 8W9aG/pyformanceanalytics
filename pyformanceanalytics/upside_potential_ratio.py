"""The PerformanceAnalytics UpsidePotentialRatio function."""
from typing import Optional

import pandas as pd
from rpy2 import robjects
from rpy2.robjects import pandas2ri

from .rimports import ensure_packages_present, PERFORMANCE_ANALYTICS_PACKAGE
from .xts import xts_from_df


def upside_potential_ratio(R: pd.DataFrame, MAR: float = 0.0, method: Optional[str] = None) -> pd.DataFrame:
    """Calculate UpsidePotentialRatio."""
    ensure_packages_present([PERFORMANCE_ANALYTICS_PACKAGE])
    if method is None:
        method = "subset"
    with robjects.local_context() as lc:
        with (robjects.default_converter + pandas2ri.converter).context():
            return robjects.conversion.get_conversion().rpy2py(robjects.r("as.data.frame").rcall(
                (
                    ("x", robjects.r("UpsidePotentialRatio").rcall(
                        (
                            ("R", xts_from_df(R)),
                            ("MAR", MAR),
                            ("method", method),
                        ),
                        lc,
                    )),
                ),
                lc,
            ))
