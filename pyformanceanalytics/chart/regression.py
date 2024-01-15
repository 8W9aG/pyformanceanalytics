"""The Performance Analytics chart.Regression function."""
from typing import Optional, List

import pandas as pd
from rpy2 import robjects
from rpy2.robjects.vectors import StrVector, IntVector

from ..rimports import ensure_packages_present, PERFORMANCE_ANALYTICS_PACKAGE
from ..xts import xts_from_df
from ..plot_img import plot_to_image


def regression(
        Ra: pd.DataFrame,
        Rb: pd.DataFrame,
        Rf: Optional[pd.DataFrame] = None,
        excess_returns: bool = False,
        reference_grid: bool = True,
        main: Optional[str] = None,
        ylab: Optional[str] = None,
        xlab: Optional[str] = None,
        colorset: Optional[List[int]] = None,
        symbolset: Optional[List[int]] = None,
        element_color: Optional[str] = None,
        legend_loc: Optional[str] = None,
        ylog: bool = False,
        fit: Optional[List[str]] = None,
        span: float = 2.0 / 3.0,
        degree: int = 1,
        family: Optional[List[str]] = None,
        evaluation: int = 50,
        legend_cex: float = 0.8,
        cex: float = 0.8,
        lwd: int = 2):
    """Calculate chart.Regression."""
    ensure_packages_present([PERFORMANCE_ANALYTICS_PACKAGE])
    if main is None:
        main = "Title"
    if colorset is None:
        colorset = list(range(1, 12))
    if symbolset is None:
        symbolset = list(range(1, 12))
    if element_color is None:
        element_color = "darkgrey"
    if fit is None:
        fit = ["loess", "linear", "conditional"]
    if family is None:
        family = ["symmetric", "gaussian"]
    with robjects.local_context() as lc:
        return plot_to_image(lambda: robjects.r("chart.Regression").rcall(
            (
                ("Ra", xts_from_df(Ra)),
                ("Rb", xts_from_df(Rb)),
                ("Rf", 0 if Rf is None else xts_from_df(Rf)),
                ("excess.returns", excess_returns),
                ("reference.grid", reference_grid),
                ("main", main),
                ("ylab", ylab),
                ("xlab", xlab),
                ("colorset", IntVector(colorset)),
                ("symbolset", IntVector(symbolset)),
                ("element.color", element_color),
                ("legend.loc", legend_loc),
                ("ylog", ylog),
                ("fit", StrVector(fit)),
                ("span", span),
                ("degree", degree),
                ("family", StrVector(family)),
                ("evaluation", evaluation),
                ("legend.cex", legend_cex),
                ("cex", cex),
                ("lwd", lwd),
            ),
            lc,
        ))
