"""The PerformanceAnalytics RPESE.control function."""
from typing import Optional

import pandas as pd
from rpy2 import robjects
from rpy2.robjects import pandas2ri

from ..rimports import ensure_packages_present, PERFORMANCE_ANALYTICS_PACKAGE, PKG_PACKAGE


def control(estimator: str, se_method: Optional[str] = None, clean_outliers: Optional[bool] = None, fitting_method: Optional[str] = None, freq_include: Optional[str] = None, freq_par: Optional[float] = None, a: Optional[float] = None, b: Optional[float] = None) -> pd.DataFrame:
    """Calculate RPESE.control."""
    ensure_packages_present([PERFORMANCE_ANALYTICS_PACKAGE, PKG_PACKAGE])
    with robjects.local_context() as lc:
        with (robjects.default_converter + pandas2ri.converter).context():
            return robjects.conversion.get_conversion().rpy2py(robjects.r("as.data.frame").rcall(
                (
                    ("x", robjects.r("RPESE.control").rcall(
                        (
                            ("estimator", estimator),
                            ("se.method", se_method),
                            ("cleanOutliers", clean_outliers),
                            ("fitting.method", fitting_method),
                            ("freq.include", freq_include),
                            ("freq.par", freq_par),
                            ("a", a),
                            ("b", b),
                        ),
                        lc,
                    )),
                ),
                lc,
            ))
