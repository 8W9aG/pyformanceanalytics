"""The PerformanceAnalytics table.SFM function."""
from typing import Optional, List

import pandas as pd
from rpy2 import robjects
from rpy2.robjects import pandas2ri
from rpy2.robjects.vectors import IntVector, StrVector

from ..rimports import ensure_packages_present, PERFORMANCE_ANALYTICS_PACKAGE
from ..xts import xts_from_df


def sfm(Ra: pd.DataFrame, Rb: pd.DataFrame, Rf: Optional[pd.DataFrame] = None, digits: int = 4) -> pd.DataFrame:
    """Calculate table.SFM."""
    ensure_packages_present([PERFORMANCE_ANALYTICS_PACKAGE])
    with robjects.local_context() as lc:
        with (robjects.default_converter + pandas2ri.converter).context():
            return robjects.conversion.get_conversion().rpy2py(robjects.r("as.data.frame").rcall(
                (
                    ("x", robjects.r("table.SFM").rcall(
                        (
                            ("Ra", xts_from_df(Ra)),
                            ("Rb", xts_from_df(Rb)),
                            ("Rf", 0 if Rf is None else xts_from_df(Rf)),
                            ("digits", digits),
                        ),
                        lc,
                    )),
                ),
                lc,
            ))
