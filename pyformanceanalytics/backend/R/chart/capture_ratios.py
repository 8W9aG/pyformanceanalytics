"""The Performance Analytics chart.CaptureRatios function."""
# pylint: disable=too-many-arguments
from __future__ import annotations

import pandas as pd
from PIL import Image
from rpy2 import robjects as ro

from ..plot_img import plot_to_image
from ..rimports import PERFORMANCE_ANALYTICS_PACKAGE, ensure_packages_present
from ..xts import xts_from_df


def CaptureRatios(
    Ra: pd.DataFrame,
    Rb: pd.DataFrame,
    plot_width: int,
    plot_height: int,
    main: (str | None) = None,
    add_names: bool = True,
    xlab: (str | None) = None,
    ylab: (str | None) = None,
    colorset: int = 1,
    symbolset: int = 1,
    legend_loc: (str | None) = None,
    xlim: (float | None) = None,
    ylim: (float | None) = None,
    cex_legend: int = 1,
    cex_axis: float = 0.8,
    cex_main: int = 1,
    cex_lab: int = 1,
    element_color: (str | None) = None,
    benchmark_color: (str | None) = None,
) -> Image.Image:
    """Calculate chart.CaptureRatios."""
    ensure_packages_present([PERFORMANCE_ANALYTICS_PACKAGE])
    if main is None:
        main = "Capture Ratio"
    if xlab is None:
        xlab = "Downside Capture"
    if ylab is None:
        ylab = "Upside Capture"
    if element_color is None:
        element_color = "darkgray"
    if benchmark_color is None:
        benchmark_color = "darkgray"
    with ro.local_context() as lc:
        return plot_to_image(
            lambda: ro.r("chart.CaptureRatios").rcall(  # type: ignore
                (
                    ("Ra", xts_from_df(Ra)),
                    ("Rb", xts_from_df(Rb)),
                    ("main", main),
                    ("add.names", add_names),
                    ("xlab", xlab),
                    ("ylab", ylab),
                    ("colorset", colorset),
                    ("symbolset", symbolset),
                    ("legend.loc", legend_loc),
                    ("xlim", xlim),
                    ("ylim", ylim),
                    ("cex.legend", cex_legend),
                    ("cex.axis", cex_axis),
                    ("cex.main", cex_main),
                    ("cex.lab", cex_lab),
                    ("element.color", element_color),
                    ("benchmark.color", benchmark_color),
                ),
                lc,
            ),
            plot_width,
            plot_height,
        )
