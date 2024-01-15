"""The Performance Analytics chart.Boxplot function."""
from typing import Optional, List

import pandas as pd
from rpy2 import robjects
from rpy2.robjects.vectors import StrVector

from ..rimports import ensure_packages_present, PERFORMANCE_ANALYTICS_PACKAGE, GGPLOT2_PACKAGE
from ..xts import xts_from_df
from ..ggplot_img import ggplot_to_image


def boxplot(
        R: pd.DataFrame,
        names: bool = True,
        as_tufte: bool = True,
        sort_by: Optional[List[Optional[str]]] = None,
        colorset: Optional[str] = None,
        symbol_color: Optional[str] = None, 
        mean_symbol: int = 1,
        median_symbol: Optional[str] = None,
        outlier_symbol: int = 1,
        show_data: Optional[List[int]] = None,
        add_mean: bool = True,
        sort_ascending: bool = False,
        xlab: Optional[str] = None,
        main: Optional[str] = None,
        element_color: Optional[str] = None):
    """Calculate chart.Boxplot."""
    ensure_packages_present([PERFORMANCE_ANALYTICS_PACKAGE, GGPLOT2_PACKAGE])
    if sort_by is None:
        sort_by = [None, "mean", "median", "variance"]
    if colorset is None:
        colorset = "black"
    if symbol_color is None:
        symbol_color = "red"
    if median_symbol is None:
        median_symbol = "|"
    if xlab is None:
        xlab = "Returns"
    if main is None:
        main = "Return Distribution Comparison"
    if element_color is None:
        element_color = "darkgrey"
    with robjects.local_context() as lc:
        plt = robjects.r("chart.Boxplot").rcall(
            (
                ("R", xts_from_df(R)),
                ("names", names),
                ("as.Tufte", as_tufte),
                ("plot.engine", "ggplot2"),
                ("sort.by", StrVector(sort_by)),
                ("colorset", colorset),
                ("symbol.color", symbol_color),
                ("mean.symbol", mean_symbol),
                ("median.symbol", median_symbol),
                ("outlier.symbol", outlier_symbol),
                ("show.data", None if show_data is None else StrVector(show_data)),
                ("add.mean", add_mean),
                ("sort.ascending", sort_ascending),
                ("xlab", xlab),
                ("main", main),
                ("element.color", element_color),
            ),
            lc,
        )
        return ggplot_to_image(plt)
