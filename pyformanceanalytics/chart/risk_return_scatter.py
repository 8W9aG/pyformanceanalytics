"""The Performance Analytics chart.RiskReturnScatter function."""
from typing import Optional, List

import pandas as pd
from rpy2 import robjects
from rpy2.robjects.vectors import StrVector, IntVector

from ..rimports import ensure_packages_present, PERFORMANCE_ANALYTICS_PACKAGE
from ..xts import xts_from_df
from ..plot_img import plot_to_image


def risk_return_scatter(
        R: pd.DataFrame,
        Rf: Optional[pd.DataFrame] = None,
        main: Optional[str] = None,
        add_names: bool = True,
        xlab: Optional[str] = None,
        ylab: Optional[str] = None,
        method: Optional[str] = None,
        geometric: bool = True,
        add_sharpe: Optional[List[int]] = None,
        add_boxplots: bool = False,
        colorset: int = 1,
        symbolset: int = 1,
        element_color: Optional[str] = None,
        legend_loc: Optional[str] = None,
        xlim: Optional[float] = None,
        ylim: Optional[float] = None,
        cex_legend: int = 1,
        cex_axis: float = 0.8,
        cex_main: int = 1,
        cex_lab: int = 1):
    """Calculate chart.RiskReturnScatter."""
    ensure_packages_present([PERFORMANCE_ANALYTICS_PACKAGE])
    if main is None:
        main = "Annualized Return and Risk"
    if xlab is None:
        xlab = "Annualized Risk"
    if ylab is None:
        ylab = "Annualized Return"
    if method is None:
        method = "calc"
    if add_sharpe is None:
        add_sharpe = [1, 2, 3]
    if element_color is None:
        element_color = "darkgray"
    with robjects.local_context() as lc:
        return plot_to_image(lambda: robjects.r("chart.RiskReturnScatter").rcall(
            (
                ("R", xts_from_df(R)),
                ("Rf", 0 if Rf is None else xts_from_df(Rf)),
                ("main", main),
                ("add.names", add_names),
                ("xlab", xlab),
                ("ylab", ylab),
                ("method", method),
                ("geometric", geometric),
                ("add.sharpe", IntVector(add_sharpe)),
                ("add.boxplots", add_boxplots),
                ("colorset", colorset),
                ("symbolset", symbolset),
                ("element.color", element_color),
                ("legend.loc", legend_loc),
                ("xlim", xlim),
                ("ylim", ylim),
                ("cex.legend", cex_legend),
                ("cex.axis", cex_axis),
                ("cex.main", cex_main),
                ("cex.lab", cex_lab),
            ),
            lc,
        ))
