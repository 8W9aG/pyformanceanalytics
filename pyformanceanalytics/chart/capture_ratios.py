"""The Performance Analytics chart.CaptureRatios function."""
from typing import Optional

import pandas as pd
from rpy2 import robjects

from ..rimports import ensure_packages_present, PERFORMANCE_ANALYTICS_PACKAGE
from ..xts import xts_from_df
from ..plot_img import plot_to_image


def capture_ratios(
        Ra: pd.DataFrame,
        Rb: pd.DataFrame,
        main: Optional[str] = None,
        add_names: bool = True,
        xlab: Optional[str] = None,
        ylab: Optional[str] = None,
        colorset: int = 1,
        symbolset: int = 1,
        legend_loc: Optional[str] = None,
        xlim: Optional[float] = None,
        ylim: Optional[float] = None,
        cex_legend: int = 1,
        cex_axis: float = 0.8,
        cex_main: int = 1,
        cex_lab: int = 1,
        element_color: Optional[str] = None,
        benchmark_color: Optional[str] = None):
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
    with robjects.local_context() as lc:
        return plot_to_image(lambda: robjects.r("chart.CaptureRatios").rcall(
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
        ))
