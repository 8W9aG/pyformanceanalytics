"""The PerformanceAnalytics Omega function."""
from typing import Optional

import pandas as pd
from rpy2 import robjects
from rpy2.robjects import pandas2ri

from .rimports import ensure_packages_present, PERFORMANCE_ANALYTICS_PACKAGE
from .xts import xts_from_df


def omega(
        R: pd.DataFrame,
        L: float = 0.0,
        method: Optional[str] = None,
        output: Optional[str] = None,
        Rf: Optional[pd.DataFrame] = None,
        SE: bool = False) -> pd.DataFrame:
    """Calculate Omega."""
    ensure_packages_present([PERFORMANCE_ANALYTICS_PACKAGE])
    if method is None:
        method = "simple"
    if output is None:
        output = "point"
    with robjects.local_context() as lc:
        with (robjects.default_converter + pandas2ri.converter).context():
            return robjects.conversion.get_conversion().rpy2py(robjects.r("as.data.frame").rcall(
                (
                    ("x", robjects.r("Omega").rcall(
                        (
                            ("R", xts_from_df(R)),
                            ("L", L),
                            ("method", method),
                            ("output", output),
                            ("Rf", 0 if Rf is None else xts_from_df(Rf)),
                            ("SE", SE),
                        ),
                        lc,
                    )),
                ),
                lc,
            ))
