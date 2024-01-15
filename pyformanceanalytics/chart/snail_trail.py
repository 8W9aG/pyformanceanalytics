"""The Performance Analytics chart.SnailTrail function."""
from typing import Optional, List

import pandas as pd
from rpy2 import robjects
from rpy2.robjects.vectors import StrVector, IntVector

from ..rimports import ensure_packages_present, PERFORMANCE_ANALYTICS_PACKAGE
from ..xts import xts_from_df
from ..plot_img import plot_to_image


def snail_trail(
        R: pd.DataFrame,
        Rf: Optional[pd.DataFrame] = None,
        main: Optional[str] = None,
        add_names: Optional[List[str]] = None,
        xlab: Optional[str] = None,
        ylab: Optional[str] = None,
        add_sharpe: Optional[List[int]] = None,
        colorset: Optional[List[int]] = None,
        symbolset: int = 16,
        legend_loc: Optional[str] = None,
        xlim: Optional[float] = None,
        ylim: Optional[float] = None,
        width: int = 12,
        stepsize: int = 12,
        lty: int = 1,
        lwd: int = 2,
        cex_axis: float = 0.8,
        cex_main: int = 1,
        cex_lab: int = 1,
        cex_text: float = 0.8,
        cex_legend: float = 0.8,
        element_color: Optional[str] = None):
    """Calculate chart.SnailTrail."""
    ensure_packages_present([PERFORMANCE_ANALYTICS_PACKAGE])
    if main is None:
        main = "Annualized Return and Risk"
    if add_names is None:
        add_names = ["all", "lastonly", "firstandlast", "none"]
    if xlab is None:
        xlab = "Annualized Risk"
    if ylab is None:
        ylab = "Annualized Return"
    if add_sharpe is None:
        add_sharpe = [1, 2, 3]
    if colorset is None:
        colorset = list(range(1, 12))
    if element_color is None:
        element_color = "darkgray"
    with robjects.local_context() as lc:
        return plot_to_image(lambda: robjects.r("chart.SnailTrail").rcall(
            (
                ("R", xts_from_df(R)),
                ("Rf", 0 if Rf is None else xts_from_df(Rf)),
                ("main", main),
                ("add.names", StrVector(add_names)),
                ("xlab", xlab),
                ("ylab", ylab),
                ("add.sharpe", IntVector(add_sharpe)),
                ("colorset", IntVector(colorset)),
                ("symbolset", symbolset),
                ("legend.loc", legend_loc),
                ("xlim", xlim),
                ("ylim", ylim),
                ("width", width),
                ("stepsize", stepsize),
                ("lty", lty),
                ("lwd", lwd),
                ("cex.axis", cex_axis),
                ("cex.main", cex_main),
                ("cex.lab", cex_lab),
                ("cex.text", cex_text),
                ("cex.legend", cex_legend),
                ("element.color", element_color),
            ),
            lc,
        ))
