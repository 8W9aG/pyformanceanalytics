"""The PerformanceAnalytics ETL function."""
from typing import Optional, List

import numpy as np
import pandas as pd
from rpy2 import robjects
from rpy2.robjects import pandas2ri, numpy2ri
from rpy2.robjects.vectors import FloatVector

from .rimports import ensure_packages_present, PERFORMANCE_ANALYTICS_PACKAGE
from .xts import xts_from_df


def ETL(
        R: pd.DataFrame,
        p: float = 0.95,
        method: Optional[str] = None,
        clean: Optional[str] = None,
        portfolio_method: Optional[str] = None,
        weights: Optional[List[float]] = None,
        mu: Optional[List[float]] = None,
        sigma: Optional[np.ndarray] = None,
        m3: Optional[np.ndarray] = None,
        m4: Optional[np.ndarray] = None,
        invert: bool = True,
        operational: bool = True,
        SE: bool = False) -> pd.DataFrame:
    """Calculate ETL."""
    ensure_packages_present([PERFORMANCE_ANALYTICS_PACKAGE])
    if method is None:
        method = "modified"
    if clean is None:
        clean = "none"
    if portfolio_method is None:
        portfolio_method = "single"
    with robjects.local_context() as lc:
        with (robjects.default_converter + numpy2ri.converter + pandas2ri.converter).context():
            return robjects.conversion.get_conversion().rpy2py(robjects.r("as.data.frame").rcall(
                (
                    ("x", robjects.r("ETL").rcall(
                        (
                            ("R", xts_from_df(R)),
                            ("p", p),
                            ("method", method),
                            ("clean", clean),
                            ("weights", None if weights is None else FloatVector(weights)),
                            ("mu", None if mu is None else FloatVector(mu)),
                            ("sigma", sigma),
                            ("m3", m3),
                            ("m4", m4),
                            ("invert", invert),
                            ("operational", operational),
                            ("SE", SE),
                        ),
                        lc,
                    )),
                ),
                lc,
            ))
