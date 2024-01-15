"""The PerformanceAnalytics M3.struct function."""
from typing import Optional

import numpy as np
import pandas as pd
from rpy2 import robjects
from rpy2.robjects import pandas2ri, numpy2ri

from ..rimports import ensure_packages_present, PERFORMANCE_ANALYTICS_PACKAGE
from ..xts import xts_from_df


def struct(R: pd.DataFrame, struct: Optional[str] = None, f: Optional[pd.DataFrame] = None, unbiased_marg: bool = False, as_mat: bool = True) -> pd.DataFrame:
    """Calculate M3.struct."""
    ensure_packages_present([PERFORMANCE_ANALYTICS_PACKAGE])
    if struct is None:
        struct = "Indep"
    with robjects.local_context() as lc:
        with (robjects.default_converter + numpy2ri.converter + pandas2ri.converter).context():
            return robjects.conversion.get_conversion().rpy2py(robjects.r("as.data.frame").rcall(
                (
                    ("x", robjects.r("M3.struct").rcall(
                        (
                            ("R", xts_from_df(R)),
                            ("struct", struct),
                            ("f", f),
                            ("unbiasedMarg", unbiased_marg),
                            ("as.mat", as_mat),
                        ),
                        lc,
                    )),
                ),
                lc,
            ))
