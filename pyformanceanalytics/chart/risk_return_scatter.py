"""The Performance Analytics chart.RiskReturnScatter function."""
# pylint: disable=too-many-arguments
from __future__ import annotations

import pandas as pd
from PIL import Image

from ..backend.backend import Backend
from ..backend.R.chart.risk_return_scatter import \
    RiskReturnScatter as RRiskReturnScatter


def RiskReturnScatter(
    R: pd.DataFrame,
    Rf: (pd.DataFrame | float) = 0.0,
    main: (str | None) = None,
    add_names: bool = True,
    xlab: (str | None) = None,
    ylab: (str | None) = None,
    method: (str | None) = None,
    geometric: bool = True,
    add_sharpe: (list[int] | None) = None,
    add_boxplots: bool = False,
    colorset: int = 1,
    symbolset: int = 1,
    element_color: (str | None) = None,
    legend_loc: (str | None) = None,
    xlim: (float | None) = None,
    ylim: (float | None) = None,
    cex_legend: int = 1,
    cex_axis: float = 0.8,
    cex_main: int = 1,
    cex_lab: int = 1,
    plot_width: int = 512,
    plot_height: int = 512,
    backend: Backend = Backend.R,
) -> Image.Image:
    """Calculate chart.RiskReturnScatter."""
    if backend == Backend.R:
        return RRiskReturnScatter(
            R,
            plot_width,
            plot_height,
            Rf,
            main=main,
            add_names=add_names,
            xlab=xlab,
            ylab=ylab,
            method=method,
            geometric=geometric,
            add_sharpe=add_sharpe,
            add_boxplots=add_boxplots,
            colorset=colorset,
            symbolset=symbolset,
            element_color=element_color,
            legend_loc=legend_loc,
            xlim=xlim,
            ylim=ylim,
            cex_legend=cex_legend,
            cex_axis=cex_axis,
            cex_main=cex_main,
            cex_lab=cex_lab,
        )
    raise NotImplementedError(
        f"Backend {backend.value} not implemented for chart.RiskReturnScatter"
    )
