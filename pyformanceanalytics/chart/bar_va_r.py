"""The Performance Analytics chart.BarVaR function."""
from typing import Optional, List

import pandas as pd
from rpy2 import robjects
from rpy2.robjects.vectors import StrVector

from ..rimports import ensure_packages_present, PERFORMANCE_ANALYTICS_PACKAGE, GGPLOT2_PACKAGE
from ..xts import xts_from_df
from ..plot_img import plot_to_image
from ..ggplot_img import ggplot_to_image


def bar_va_r(
        R: pd.DataFrame,
        width: int = 0,
        gap: int = 12,
        methods: Optional[List[str]] = None,
        p: float = 0.95,
        clean: Optional[List[str]] = None,
        all: bool = False,
        show_clean: bool = False,
        show_horizontal: bool = False,
        show_symmetric: bool = False,
        show_endvalue: bool = False,
        show_greenredbars: bool = False,
        legend_loc: Optional[str] = None,
        lwd: int = 2,
        lty: int = 1,
        ypad: int = 0,
        legend_cex: float = 0.8):
    """Calculate chart.BarVaR."""
    ensure_packages_present([PERFORMANCE_ANALYTICS_PACKAGE, GGPLOT2_PACKAGE])
    if methods is None:
        methods = ["none"]
    if clean is None:
        clean = ["none"]
    if legend_loc is None:
        legend_loc = "bottomleft"
    with robjects.local_context() as lc:
        return plot_to_image(lambda: robjects.r("plot").rcall(
            (
                ("x", robjects.r("chart.BarVaR").rcall(
                    (
                        ("R", xts_from_df(R)),
                        ("width", width),
                        ("gap", gap),
                        ("methods", StrVector(methods)),
                        ("p", p),
                        ("clean", StrVector(clean)),
                        ("all", all),
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
                )),
            ),
            lc,
        ))
