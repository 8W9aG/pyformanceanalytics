"""The Performance Analytics chart.BarVaR function."""
# pylint: disable=too-many-arguments
from __future__ import annotations

import pandas as pd
from PIL import Image
from rpy2 import robjects as ro

from ..plot_img import plot_ro, plot_to_image
from ..rimports import (GGPLOT2_PACKAGE, PERFORMANCE_ANALYTICS_PACKAGE,
                        ensure_packages_present)
from ..xts import xts_from_df


def BarVaR(
    R: pd.DataFrame,
    methods: list[str],
    clean: str,
    plot_width: int,
    plot_height: int,
    width: int = 0,
    gap: int = 12,
    p: float = 0.95,
    all_: bool = False,
    show_clean: bool = False,
    show_horizontal: bool = False,
    show_symmetric: bool = False,
    show_endvalue: bool = False,
    show_greenredbars: bool = False,
    legend_loc: (str | None) = None,
    lwd: int = 2,
    lty: int = 1,
    ypad: int = 0,
    legend_cex: float = 0.8,
) -> Image.Image:
    """Calculate chart.BarVaR."""
    ensure_packages_present([PERFORMANCE_ANALYTICS_PACKAGE, GGPLOT2_PACKAGE])
    if legend_loc is None:
        legend_loc = "bottomleft"
    with ro.local_context() as lc:
        return plot_to_image(
            lambda: plot_ro(
                ro.r("chart.BarVaR").rcall(  # type: ignore
                    (
                        ("R", xts_from_df(R)),
                        ("width", width),
                        ("gap", gap),
                        ("methods", ro.vectors.StrVector(methods)),
                        ("p", p),
                        ("clean", ro.vectors.StrVector([clean])),
                        ("all", all_),
                        ("show.clean", show_clean),
                        ("show.horizontal", show_horizontal),
                        ("show.symmetric", show_symmetric),
                        ("show.endvalue", show_endvalue),
                        ("show.greenredbars", show_greenredbars),
                        ("legend.loc", legend_loc),
                        ("lwd", lwd),
                        ("lty", lty),
                        ("ypad", ypad),
                        ("legend.cex", legend_cex),
                        ("plot.engine", "default"),
                    ),
                    lc,
                ),
                lc,
            ),
            plot_width,
            plot_height,
        )
