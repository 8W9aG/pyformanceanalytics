"""The Performance Analytics chart.SnailTrail function."""
# pylint: disable=too-many-arguments
from __future__ import annotations

import pandas as pd
from PIL import Image
from rpy2 import robjects as ro

from ..plot_img import plot_to_image
from ..rimports import PERFORMANCE_ANALYTICS_PACKAGE, ensure_packages_present
from ..xts import xts_from_df


def SnailTrail(
    R: pd.DataFrame,
    add_names: str,
    plot_width: int,
    plot_height: int,
    Rf: (pd.DataFrame | float),
    main: (str | None) = None,
    xlab: (str | None) = None,
    ylab: (str | None) = None,
    add_sharpe: (list[int] | None) = None,
    colorset: (list[int] | None) = None,
    symbolset: int = 16,
    legend_loc: (str | None) = None,
    xlim: (float | None) = None,
    ylim: (float | None) = None,
    width: int = 12,
    stepsize: int = 12,
    lty: int = 1,
    lwd: int = 2,
    cex_axis: float = 0.8,
    cex_main: int = 1,
    cex_lab: int = 1,
    cex_text: float = 0.8,
    cex_legend: float = 0.8,
    element_color: (str | None) = None,
) -> Image.Image:
    """Calculate chart.SnailTrail."""
    ensure_packages_present([PERFORMANCE_ANALYTICS_PACKAGE])
    if main is None:
        main = "Annualized Return and Risk"
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
    with ro.local_context() as lc:
        return plot_to_image(
            lambda: ro.r("chart.SnailTrail").rcall(  # type: ignore
                (
                    ("R", xts_from_df(R)),
                    ("Rf", xts_from_df(Rf) if isinstance(Rf, pd.DataFrame) else Rf),
                    ("main", main),
                    ("add.names", ro.vectors.StrVector([add_names])),
                    ("xlab", xlab),
                    ("ylab", ylab),
                    ("add.sharpe", ro.vectors.IntVector(add_sharpe)),
                    ("colorset", ro.vectors.IntVector(colorset)),
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
            ),
            plot_width,
            plot_height,
        )
