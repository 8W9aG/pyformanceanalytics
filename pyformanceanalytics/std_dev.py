"""The PerformanceAnalytics StdDev function."""
from typing import Optional

import pandas as pd
from rpy2 import robjects
from rpy2.robjects import pandas2ri

from .rimports import ensure_packages_present, PERFORMANCE_ANALYTICS_PACKAGE
from .xts import xts_from_df


def std_dev(R: pd.DataFrame, clean: Optional[str] = None, portfolio_method: Optional[str] = None, weights: Optional[pd.DataFrame] = None, mu: Optional[pd.DataFrame] = None, sigma: Optional[pd.DataFrame] = None, use: Optional[str] = None, method: Optional[str] = None, SE: bool = False) -> pd.DataFrame:
    """Calculate StdDev."""
    ensure_packages_present([PERFORMANCE_ANALYTICS_PACKAGE])
    if clean is None:
        clean = "none"
    if portfolio_method is None:
        portfolio_method = "single"
    if use is None:
        use = "everything"
    if method is None:
        method = "pearson"
    with robjects.local_context() as lc:
        with (robjects.default_converter + pandas2ri.converter).context():
            return robjects.conversion.get_conversion().rpy2py(robjects.r("as.data.frame").rcall(
                (
                    ("x", robjects.r("StdDev").rcall(
                        (
                            ("R", xts_from_df(R)),
                            ("clean", clean),
                            ("portfolio_method", portfolio_method),
                            ("weights", weights),
                            ("mu", mu),
                            ("sigma", sigma),
                            ("use", use),
                            ("method", method),
                            ("SE", SE),
                        ),
                        lc,
                    )),
                ),
                lc,
            ))
