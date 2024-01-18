"""The Performance Analytics chart.VaRSensitivity function."""
# pylint: disable=too-many-arguments
from __future__ import annotations

import pandas as pd
from PIL import Image

from ..backend.backend import Backend
from ..backend.R.chart.va_r_sensitivity import \
    VaRSensitivity as RVaRSensitivity
from .clean import Clean
from .va_r_sensitivity_methods import VaRSensitivityMethods


def VaRSensitivity(
    R: pd.DataFrame,
    methods: (list[str | VaRSensitivityMethods] | None) = None,
    clean: (str | Clean | None) = None,
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
    plot_width: int = 512,
    plot_height: int = 512,
    backend: Backend = Backend.R,
) -> Image.Image:
    """Calculate chart.VaRSensitivity."""
    if methods is None:
        methods = [
            VaRSensitivityMethods.GAUSSIANVAR,
            VaRSensitivityMethods.MODIFIEDVAR,
            VaRSensitivityMethods.HISTORICALVAR,
            VaRSensitivityMethods.GAUSSIANES,
            VaRSensitivityMethods.MODIFIEDES,
            VaRSensitivityMethods.HISTORICALES,
        ]
    if clean is None:
        clean = Clean.NONE
    if backend == Backend.R:
        if isinstance(clean, Clean):
            clean = clean.value
        return RVaRSensitivity(
            R,
            [x.value if isinstance(x, VaRSensitivityMethods) else x for x in methods],
            clean,
            plot_width,
            plot_height,
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
