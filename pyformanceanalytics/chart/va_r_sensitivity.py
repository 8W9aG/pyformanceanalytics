"""The Performance Analytics chart.VaRSensitivity function."""
# pylint: disable=too-many-arguments
from __future__ import annotations

import pandas as pd
from PIL import Image

from ..backend.backend import Backend
from ..backend.R.chart.va_r_sensitivity import \
    VaRSensitivity as RVaRSensitivity


def VaRSensitivity(
    R: pd.DataFrame,
    methods: (list[str] | None) = None,
    clean: (list[str] | None) = None,
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
    backend: Backend = Backend.R,
) -> Image.Image:
    """Calculate chart.VaRSensitivity."""
    if backend == Backend.R:
        return RVaRSensitivity(
            R,
            methods=methods,
            clean=clean,
            element_color=element_color,
            reference_grid=reference_grid,
            xlab=xlab,
            ylab=ylab,
            type_=type_,
            lty=lty,
            lwd=lwd,
            colorset=colorset,
            pch=pch,
            legend_loc=legend_loc,
            cex_legend=cex_legend,
            main=main,
            ylim=ylim,
        )
    raise NotImplementedError(
        f"Backend {backend.value} not implemented for chart.VaRSensitivity"
    )
