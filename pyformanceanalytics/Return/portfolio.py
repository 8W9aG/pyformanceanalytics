"""The PerformanceAnalytics Return.portfolio function."""
from __future__ import annotations

import pandas as pd

from ..backend.backend import Backend
from ..backend.R.Return.portfolio import portfolio as Rportfolio
from .portfolio_rebalance_on import PortfolioRebalanceOn


def portfolio(
    R: pd.DataFrame,
    weights: (pd.DataFrame | None) = None,
    wealth_index: bool = False,
    contribution: bool = False,
    geometric: bool = True,
    rebalance_on: (str | PortfolioRebalanceOn | None) = None,
    value: int = 1,
    verbose: bool = False,
    backend: Backend = Backend.R,
) -> pd.DataFrame:
    """Calculate Return.portfolio."""
    if rebalance_on is None:
        rebalance_on = PortfolioRebalanceOn.YEARS
    if backend == Backend.R:
        if isinstance(rebalance_on, PortfolioRebalanceOn):
            rebalance_on = rebalance_on.value
        return Rportfolio(
            R,
            rebalance_on,
            weights=weights,
            wealth_index=wealth_index,
            contribution=contribution,
            geometric=geometric,
            value=value,
            verbose=verbose,
        )
    raise NotImplementedError(
        f"Backend {backend.value} not implemented for Return.portfolio"
    )
