"""The Performance Analytics chart.RelativePerformance function."""
# pylint: disable=too-many-arguments
from __future__ import annotations

import pandas as pd
from PIL import Image
from rpy2 import robjects as ro

from ..plot_img import plot_ro, plot_to_image
from ..rimports import PERFORMANCE_ANALYTICS_PACKAGE, ensure_packages_present
from ..xts import xts_from_df


def RelativePerformance(
    Ra: pd.DataFrame,
    Rb: pd.DataFrame,
    plot_width: int,
    plot_height: int,
    main: (str | None) = None,
    xaxis: bool = True,
    colorset: (list[int] | None) = None,
    legend_loc: (str | None) = None,
    ylog: bool = False,
    element_color: (str | None) = None,
    lty: int = 1,
    cex_legend: float = 0.7,
) -> Image.Image:
    """Calculate chart.RelativePerformance."""
    ensure_packages_present([PERFORMANCE_ANALYTICS_PACKAGE])
    if main is None:
        main = "Relative Performance"
    if colorset is None:
        colorset = list(range(1, 12))
    if element_color is None:
        element_color = "darkgrey"
    with ro.local_context() as lc:
        return plot_to_image(
            lambda: plot_ro(
                ro.r("chart.RelativePerformance").rcall(  # type: ignore
                    (
                        ("Ra", xts_from_df(Ra)),
                        ("Rb", xts_from_df(Rb)),
                        ("main", main),
                        ("xaxis", xaxis),
                        ("colorset", ro.vectors.IntVector(colorset)),
                        ("legend.loc", legend_loc),
                        ("ylog", ylog),
                        ("element.color", element_color),
                        ("lty", lty),
                        ("cex.legend", cex_legend),
                    ),
                    lc,
                ),
                lc,
            ),
            plot_width,
            plot_height,
        )
