"""The PerformanceAnalytics VaR function."""
from typing import Optional, Union

import pandas as pd
from rpy2 import robjects
from rpy2.robjects import pandas2ri

from .rimports import ensure_packages_present, PERFORMANCE_ANALYTICS_PACKAGE
from .xts import xts_from_df


def var(
        R: Optional[pd.DataFrame] = None,
        p: float = 0.95,
        method: Optional[str] = None,
        clean: Optional[str] = None,
        portfolio_method: Optional[str] = None,
        weights: Optional[pd.DataFrame] = None,
        mu: Optional[Union[pd.DataFrame, float]] = None,
        sigma: Optional[Union[pd.DataFrame, float]] = None,
        m3: Optional[Union[pd.DataFrame, float]] = None,
        m4: Optional[Union[pd.DataFrame, float]] = None,
        invert: bool = False,
        SE: bool = False) -> pd.DataFrame:
    """Calculate VaR."""
    ensure_packages_present([PERFORMANCE_ANALYTICS_PACKAGE])
    if method is None:
        method = "modified"
    if clean is None:
        clean = "none"
    if portfolio_method is None:
        portfolio_method = "single"
    with robjects.local_context() as lc:
        with (robjects.default_converter + pandas2ri.converter).context():
            return robjects.conversion.get_conversion().rpy2py(robjects.r("as.data.frame").rcall(
                (
                    ("x", robjects.r("VaR").rcall(
                        (
                            ("R", None if R is None else xts_from_df(R)),
                            ("p", p),
                            ("method", method),
                            ("clean", clean),
                            ("portfolio_method", portfolio_method),
                            ("weights", weights),
                            ("mu", mu),
                            ("sigma", sigma),
                            ("m3", m3),
                            ("m4", m4),
                            ("invert", invert),
                            ("SE", SE),
                        ),
                        lc,
                    )),
                ),
                lc,
            ))
