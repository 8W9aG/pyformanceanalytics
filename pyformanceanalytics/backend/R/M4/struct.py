"""The PerformanceAnalytics M4.struct function."""
from __future__ import annotations

import numpy as np
import pandas as pd
from rpy2 import robjects as ro
from rpy2.robjects import numpy2ri

from ..rimports import PERFORMANCE_ANALYTICS_PACKAGE, ensure_packages_present
from ..xts import xts_from_df


def struct(
    R: pd.DataFrame,
    struct_type: str,
    f: (pd.DataFrame | None) = None,
    as_mat: bool = True,
) -> np.ndarray:
    """Calculate M4.struct."""
    ensure_packages_present([PERFORMANCE_ANALYTICS_PACKAGE])
    with ro.local_context() as lc:
        with (ro.default_converter + numpy2ri.converter).context():
            return np.array(
                ro.r("M4.struct").rcall(  # type: ignore
                    (
                        ("R", xts_from_df(R)),
                        ("struct", struct_type),
                        ("f", f),
                        ("as.mat", as_mat),
                    ),
                    lc,
                )
            )
