"""The Performance Analytics chart.RiskReturnScatter function."""
# pylint: disable=too-many-arguments
from __future__ import annotations

import pandas as pd
from PIL import Image
from rpy2 import robjects as ro

from ..plot_img import plot_to_image
from ..rimports import PERFORMANCE_ANALYTICS_PACKAGE, ensure_packages_present
from ..xts import xts_from_df


def RiskReturnScatter(
    R: pd.DataFrame,
    plot_width: int,
    plot_height: int,
    Rf: (pd.DataFrame | float),
    main: (str | None) = None,
    add_names: bool = True,
    xlab: (str | None) = None,
    ylab: (str | None) = None,
    method: (str | None) = None,
    geometric: bool = True,
    add_sharpe: (list[int] | None) = None,
    add_boxplots: bool = False,
    colorset: int = 1,
    symbolset: int = 1,
    element_color: (str | None) = None,
    legend_loc: (str | None) = None,
    xlim: (float | None) = None,
    ylim: (float | None) = None,
    cex_legend: int = 1,
    cex_axis: float = 0.8,
    cex_main: int = 1,
    cex_lab: int = 1,
) -> Image.Image:
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
    with ro.local_context() as lc:
        return plot_to_image(
            lambda: ro.r("chart.RiskReturnScatter").rcall(  # type: ignore
                (
                    ("R", xts_from_df(R)),
                    ("Rf", xts_from_df(Rf) if isinstance(Rf, pd.DataFrame) else Rf),
                    ("main", main),
                    ("add.names", add_names),
                    ("xlab", xlab),
                    ("ylab", ylab),
                    ("method", method),
                    ("geometric", geometric),
                    ("add.sharpe", ro.vectors.IntVector(add_sharpe)),
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
            ),
            plot_width,
            plot_height,
        )
