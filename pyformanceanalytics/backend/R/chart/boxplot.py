"""The Performance Analytics chart.Boxplot function."""
# pylint: disable=too-many-arguments
from __future__ import annotations

import pandas as pd
from PIL import Image
from rpy2 import robjects as ro

from ..ggplot_img import ggplot_to_image
from ..rimports import (GGPLOT2_PACKAGE, PERFORMANCE_ANALYTICS_PACKAGE,
                        ensure_packages_present)
from ..xts import xts_from_df


def Boxplot(
    R: pd.DataFrame,
    plot_width: int,
    plot_height: int,
    names: bool = True,
    as_tufte: bool = True,
    sort_by: (str | None) = None,
    colorset: (str | None) = None,
    symbol_color: (str | None) = None,
    mean_symbol: int = 1,
    median_symbol: (str | None) = None,
    outlier_symbol: int = 1,
    show_data: (list[int] | None) = None,
    add_mean: bool = True,
    sort_ascending: bool = False,
    xlab: (str | None) = None,
    main: (str | None) = None,
    element_color: (str | None) = None,
) -> Image.Image:
    """Calculate chart.Boxplot."""
    ensure_packages_present([PERFORMANCE_ANALYTICS_PACKAGE, GGPLOT2_PACKAGE])
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
    with ro.local_context() as lc:
        return ggplot_to_image(
            ro.r("chart.Boxplot").rcall(  # type: ignore
                (
                    ("R", xts_from_df(R)),
                    ("names", names),
                    ("as.Tufte", as_tufte),
                    ("plot.engine", "ggplot2"),
                    ("sort.by", sort_by),
                    ("colorset", colorset),
                    ("symbol.color", symbol_color),
                    ("mean.symbol", mean_symbol),
                    ("median.symbol", median_symbol),
                    ("outlier.symbol", outlier_symbol),
                    (
                        "show.data",
                        None if show_data is None else ro.vectors.StrVector(show_data),
                    ),
                    ("add.mean", add_mean),
                    ("sort.ascending", sort_ascending),
                    ("xlab", xlab),
                    ("main", main),
                    ("element.color", element_color),
                ),
                lc,
            ),
            plot_width,
            plot_height,
        )
