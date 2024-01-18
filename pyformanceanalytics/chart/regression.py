"""The Performance Analytics chart.Regression function."""
# pylint: disable=too-many-arguments
from __future__ import annotations

import pandas as pd
from PIL import Image

from ..backend.backend import Backend
from ..backend.R.chart.regression import Regression as RRegression
from .regression_family import RegressionFamily
from .regression_fit import RegressionFit


def Regression(
    Ra: pd.DataFrame,
    Rb: pd.DataFrame,
    Rf: (pd.DataFrame | float) = 0.0,
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
    fit: (str | RegressionFit | None) = None,
    span: float = 2.0 / 3.0,
    degree: int = 1,
    family: (str | RegressionFamily | None) = None,
    evaluation: int = 50,
    legend_cex: float = 0.8,
    cex: float = 0.8,
    lwd: int = 2,
    plot_width: int = 512,
    plot_height: int = 512,
    backend: Backend = Backend.R,
) -> Image.Image:
    """Calculate chart.Regression."""
    if fit is None:
        fit = RegressionFit.LOESS
    if family is None:
        family = RegressionFamily.SYMMETRIC
    if backend == Backend.R:
        if isinstance(fit, RegressionFit):
            fit = fit.value
        if isinstance(family, RegressionFamily):
            family = family.value
        return RRegression(
            Ra,
            Rb,
            fit,
            family,
            plot_width,
            plot_height,
            Rf,
            excess_returns=excess_returns,
            reference_grid=reference_grid,
            main=main,
            ylab=ylab,
            xlab=xlab,
            colorset=colorset,
            symbolset=symbolset,
            element_color=element_color,
            legend_loc=legend_loc,
            ylog=ylog,
            span=span,
            degree=degree,
            evaluation=evaluation,
            legend_cex=legend_cex,
            cex=cex,
            lwd=lwd,
        )
    raise NotImplementedError(
        f"Backend {backend.value} not implemented for chart.Regression"
    )
