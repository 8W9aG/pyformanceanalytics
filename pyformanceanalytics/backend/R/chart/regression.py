"""The Performance Analytics chart.Regression function."""
# pylint: disable=too-many-arguments
from __future__ import annotations

import pandas as pd
from PIL import Image
from rpy2 import robjects as ro

from ..plot_img import plot_to_image
from ..rimports import PERFORMANCE_ANALYTICS_PACKAGE, ensure_packages_present
from ..xts import xts_from_df


def Regression(
    Ra: pd.DataFrame,
    Rb: pd.DataFrame,
    fit: str,
    family: str,
    plot_width: int,
    plot_height: int,
    Rf: (pd.DataFrame | float),
    excess_returns: bool = False,
    reference_grid: bool = True,
    main: (str | None) = None,
    ylab: (str | None) = None,
    xlab: (str | None) = None,
    colorset: (list[int] | None) = None,
    symbolset: (list[int] | None) = None,
    element_color: (str | None) = None,
    legend_loc: (str | None) = None,
    ylog: bool = False,
    span: float = 2.0 / 3.0,
    degree: int = 1,
    evaluation: int = 50,
    legend_cex: float = 0.8,
    cex: float = 0.8,
    lwd: int = 2,
) -> Image.Image:
    """Calculate chart.Regression."""
    ensure_packages_present([PERFORMANCE_ANALYTICS_PACKAGE])
    if main is None:
        main = "Title"
    if colorset is None:
        colorset = list(range(1, 12))
    if symbolset is None:
        symbolset = list(range(1, 12))
    if element_color is None:
        element_color = "darkgrey"
    with ro.local_context() as lc:
        return plot_to_image(
            lambda: ro.r("chart.Regression").rcall(  # type: ignore
                (
                    ("Ra", xts_from_df(Ra)),
                    ("Rb", xts_from_df(Rb)),
                    ("Rf", xts_from_df(Rf) if isinstance(Rf, pd.DataFrame) else Rf),
                    ("excess.returns", excess_returns),
                    ("reference.grid", reference_grid),
                    ("main", main),
                    ("ylab", ylab),
                    ("xlab", xlab),
                    ("colorset", ro.vectors.IntVector(colorset)),
                    ("symbolset", ro.vectors.IntVector(symbolset)),
                    ("element.color", element_color),
                    ("legend.loc", legend_loc),
                    ("ylog", ylog),
                    ("fit", ro.vectors.StrVector([fit])),
                    ("span", span),
                    ("degree", degree),
                    ("family", ro.vectors.StrVector([family])),
                    ("evaluation", evaluation),
                    ("legend.cex", legend_cex),
                    ("cex", cex),
                    ("lwd", lwd),
                ),
                lc,
            ),
            plot_width,
            plot_height,
        )
