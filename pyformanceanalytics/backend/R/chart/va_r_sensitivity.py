"""The Performance Analytics chart.VaRSensitivity function."""
# pylint: disable=too-many-arguments
from __future__ import annotations

import pandas as pd
from PIL import Image
from rpy2 import robjects as ro

from ..plot_img import plot_to_image
from ..rimports import PERFORMANCE_ANALYTICS_PACKAGE, ensure_packages_present
from ..xts import xts_from_df


def VaRSensitivity(
    R: pd.DataFrame,
    methods: list[str],
    clean: str,
    plot_width: int,
    plot_height: int,
    element_color: (str | None) = None,
    reference_grid: bool = True,
    xlab: (str | None) = None,
    ylab: (str | None) = None,
    type_: (str | None) = None,
    lty: (list[int] | None) = None,
    lwd: int = 1,
    colorset: (list[int] | None) = None,
    pch: (list[int] | None) = None,
    legend_loc: (str | None) = None,
    cex_legend: float = 0.8,
    main: (str | None) = None,
    ylim: (float | None) = None,
) -> Image.Image:
    """Calculate chart.VaRSensitivity."""
    ensure_packages_present([PERFORMANCE_ANALYTICS_PACKAGE])
    if element_color is None:
        element_color = "darkgray"
    if xlab is None:
        xlab = "Confidence Level"
    if ylab is None:
        ylab = "Value at Risk"
    if type_ is None:
        type_ = "l"
    if lty is None:
        lty = [1, 2, 4]
    if colorset is None:
        colorset = list(range(1, 12))
    if pch is None:
        pch = list(range(1, 12))
    if legend_loc is None:
        legend_loc = "bottomleft"
    with ro.local_context() as lc:
        return plot_to_image(
            lambda: ro.r("chart.VaRSensitivity").rcall(  # type: ignore
                (
                    ("R", xts_from_df(R)),
                    ("methods", ro.vectors.StrVector(methods)),
                    ("clean", ro.vectors.StrVector([clean])),
                    ("element.color", element_color),
                    ("reference.grid", reference_grid),
                    ("xlab", xlab),
                    ("ylab", ylab),
                    ("type", type_),
                    ("lty", ro.vectors.IntVector(lty)),
                    ("lwd", lwd),
                    ("colorset", ro.vectors.IntVector(colorset)),
                    ("pch", ro.vectors.IntVector(pch)),
                    ("legend.loc", legend_loc),
                    ("cex.legend", cex_legend),
                    ("main", main),
                    ("ylim", ylim),
                ),
                lc,
            ),
            plot_width,
            plot_height,
        )
