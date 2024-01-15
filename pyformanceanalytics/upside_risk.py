"""The PerformanceAnalytics UpsideRisk function."""
from typing import Optional

import pandas as pd
from rpy2 import robjects
from rpy2.robjects import pandas2ri

from .rimports import ensure_packages_present, PERFORMANCE_ANALYTICS_PACKAGE
from .xts import xts_from_df


def upside_risk(R: pd.DataFrame, MAR: float = 0.0, method: Optional[str] = None, stat: Optional[str] = None) -> pd.DataFrame:
    """Calculate UpsideRisk."""
    ensure_packages_present([PERFORMANCE_ANALYTICS_PACKAGE])
    if method is None:
        method = "subset"
    if stat is None:
        stat = "risk"
    with robjects.local_context() as lc:
        with (robjects.default_converter + pandas2ri.converter).context():
            return robjects.conversion.get_conversion().rpy2py(robjects.r("as.data.frame").rcall(
                (
                    ("x", robjects.r("UpsideRisk").rcall(
                        (
                            ("R", xts_from_df(R)),
                            ("MAR", MAR),
                            ("method", method),
                            ("stat", stat),
                        ),
                        lc,
                    )),
                ),
                lc,
            ))
