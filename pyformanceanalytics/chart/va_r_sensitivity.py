"""The Performance Analytics chart.VaRSensitivity function."""
from typing import Optional, List

import pandas as pd
from rpy2 import robjects
from rpy2.robjects.vectors import StrVector, IntVector

from ..rimports import ensure_packages_present, PERFORMANCE_ANALYTICS_PACKAGE
from ..xts import xts_from_df
from ..plot_img import plot_to_image


def va_r_sensitivity(
        R: pd.DataFrame,
        methods: Optional[List[str]] = None,
        clean: Optional[List[str]] = None,
        element_color: Optional[str] = None,
        reference_grid: bool = True,
        xlab: Optional[str] = None,
        ylab: Optional[str] = None,
        type: Optional[str] = None,
        lty: Optional[List[str]] = None,
        lwd: int = 1,
        colorset: Optional[List[int]] = None,
        pch: Optional[List[int]] = None,
        legend_loc: Optional[str] = None,
        cex_legend: float = 0.8,
        main: Optional[str] = None,
        ylim: Optional[float] = None):
    """Calculate chart.VaRSensitivity."""
    ensure_packages_present([PERFORMANCE_ANALYTICS_PACKAGE])
    if methods is None:
        methods = ["GaussianVaR", "ModifiedVaR", "HistoricalVaR", "GaussianES", "ModifiedES", "HistoricalES"]
    if clean is None:
        clean = ["none", "boudt", "geltner"]
    if element_color is None:
        element_color = "darkgray"
    if xlab is None:
        xlab = "Confidence Level"
    if ylab is None:
        ylab = "Value at Risk"
    if type is None:
        type = "l"
    if lty is None:
        lty = [1, 2, 4]
    if colorset is None:
        colorset = list(range(1, 12))
    if pch is None:
        pch = list(range(1, 12))
    if legend_loc is None:
        legend_loc = "bottomleft"
    with robjects.local_context() as lc:
        return plot_to_image(lambda: robjects.r("chart.VaRSensitivity").rcall(
            (
                ("R", xts_from_df(R)),
                ("methods", StrVector(methods)),
                ("clean", StrVector(clean)),
                ("element.color", element_color),
                ("reference.grid", reference_grid),
                ("xlab", xlab),
                ("ylab", ylab),
                ("type", type),
                ("lty", IntVector(lty)),
                ("lwd", lwd),
                ("colorset", IntVector(colorset)),
                ("pch", IntVector(pch)),
                ("legend.loc", legend_loc),
                ("cex.legend", cex_legend),
                ("main", main),
                ("ylim", ylim),
            ),
            lc,
        ))
