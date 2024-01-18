"""The Performance Analytics chart.ECDF function."""
# pylint: disable=too-many-arguments
from __future__ import annotations

import pandas as pd
from PIL import Image
from rpy2 import robjects as ro

from ..plot_img import plot_to_image
from ..rimports import PERFORMANCE_ANALYTICS_PACKAGE, ensure_packages_present
from ..xts import xts_from_df


def ECDF(
    R: pd.DataFrame,
    plot_width: int,
    plot_height: int,
    main: (str | None) = None,
    xlab: (str | None) = None,
    ylab: (str | None) = None,
    colorset: (list[str] | None) = None,
    lwd: int = 1,
    lty: (list[int] | None) = None,
    element_color: (str | None) = None,
    xaxis: bool = True,
    yaxis: bool = True,
) -> Image.Image:
    """Calculate chart.ECDF."""
    ensure_packages_present([PERFORMANCE_ANALYTICS_PACKAGE])
    if main is None:
        main = "Empirical CDF"
    if xlab is None:
        xlab = "x"
    if ylab is None:
        ylab = "F(x)"
    if colorset is None:
        colorset = ["black", "#005AFF"]
    if lty is None:
        lty = [1, 2]
    if element_color is None:
        element_color = "darkgray"
    with ro.local_context() as lc:
        return plot_to_image(
            lambda: ro.r("chart.ECDF").rcall(  # type: ignore
                (
                    ("R", xts_from_df(R)),
                    ("main", main),
                    ("xlab", xlab),
                    ("ylab", ylab),
                    ("colorset", ro.vectors.StrVector(colorset)),
                    ("lwd", lwd),
                    ("lty", ro.vectors.IntVector(lty)),
                    ("element.color", element_color),
                    ("xaxis", xaxis),
                    ("yaxis", yaxis),
                ),
                lc,
            ),
            plot_width,
            plot_height,
        )
