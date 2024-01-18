"""The PerformanceAnalytics M3.struct function."""
from __future__ import annotations

import numpy as np
import pandas as pd
from rpy2 import robjects as ro
from rpy2.robjects import numpy2ri

from ..rimports import PERFORMANCE_ANALYTICS_PACKAGE, ensure_packages_present
from ..xts import xts_from_df


def struct(
    R: pd.DataFrame,
    struct_type: (str | None) = None,
    f: (pd.DataFrame | None) = None,
    unbiased_marg: bool = False,
    as_mat: bool = True,
) -> np.ndarray:
    """Calculate M3.struct."""
    ensure_packages_present([PERFORMANCE_ANALYTICS_PACKAGE])
    if struct_type is None:
        struct_type = "Indep"
    with ro.local_context() as lc:
        with (ro.default_converter + numpy2ri.converter).context():
            return np.array(
                ro.r("M3.struct").rcall(  # type: ignore
                    (
                        ("R", xts_from_df(R)),
                        ("struct", struct_type),
                        ("f", f),
                        ("unbiasedMarg", unbiased_marg),
                        ("as.mat", as_mat),
                    ),
                    lc,
                )
            )
