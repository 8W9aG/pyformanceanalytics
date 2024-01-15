"""The PerformanceAnalytics Return.relative function."""
from typing import Optional

import pandas as pd
from rpy2 import robjects
from rpy2.robjects import pandas2ri

from ..rimports import ensure_packages_present, PERFORMANCE_ANALYTICS_PACKAGE, PKG_PACKAGE
from ..xts import xts_from_df


def relative(Ra: pd.DataFrame, Rb: pd.DataFrame) -> pd.DataFrame:
    """Calculate Return.relative."""
    ensure_packages_present([PERFORMANCE_ANALYTICS_PACKAGE, PKG_PACKAGE])
    with robjects.local_context() as lc:
        with (robjects.default_converter + pandas2ri.converter).context():
            return robjects.conversion.get_conversion().rpy2py(robjects.r("as.data.frame").rcall(
                (
                    ("x", robjects.r("Return.relative").rcall(
                        (
                            ("Ra", xts_from_df(Ra)),
                            ("Rb", xts_from_df(Rb)),
                        ),
                        lc,
                    )),
                ),
                lc,
            ))