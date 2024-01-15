"""The PerformanceAnalytics MinTrackRecord function."""
from typing import Optional, Union

import pandas as pd
from rpy2 import robjects
from rpy2.robjects import pandas2ri

from .rimports import ensure_packages_present, PERFORMANCE_ANALYTICS_PACKAGE
from .xts import xts_from_df


def min_track_record(
        refSR: Union[pd.DataFrame, float],
        R: Optional[pd.DataFrame] = None,
        Rf: Optional[pd.DataFrame] = None,
        p: float = 0.95,
        weights: Optional[pd.DataFrame] = None,
        n: Optional[int] = None,
        sr: Optional[float] = None,
        sk: Optional[float] = None,
        kr: Optional[float] = None,
        ignore_skewness: bool = True,
        ignore_kurtosis: bool = True) -> pd.DataFrame:
    """Calculate MinTrackRecord."""
    ensure_packages_present([PERFORMANCE_ANALYTICS_PACKAGE])
    with robjects.local_context() as lc:
        with (robjects.default_converter + pandas2ri.converter).context():
            return robjects.conversion.get_conversion().rpy2py(robjects.r("as.data.frame").rcall(
                (
                    ("x", robjects.r("MinTrackRecord").rcall(
                        (
                            ("R", None if R is None else xts_from_df(R)),
                            ("Rf", 0 if Rf is None else xts_from_df(Rf)),
                            ("refSR", refSR if isinstance(refSR, float) else xts_from_df(refSR)),
                            ("p", p),
                            ("weights", None if weights is None else xts_from_df(weights)),
                            ("n", n),
                            ("sr", sr),
                            ("sk", sk),
                            ("kr", kr),
                            ("ignore_skewness", ignore_skewness),
                            ("ignore_kurtosis", ignore_kurtosis),
                        ),
                        lc,
                    )),
                ),
                lc,
            ))
