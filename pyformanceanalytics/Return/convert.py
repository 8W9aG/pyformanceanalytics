"""The PerformanceAnalytics Return.convert function."""
from __future__ import annotations

import pandas as pd

from ..backend.backend import Backend
from ..backend.R.Return.convert import convert as Rconvert


def convert(
    R: pd.DataFrame,
    destination_type: (str | None) = None,
    seed_value: (float | None) = None,
    initial: bool = True,
    backend: Backend = Backend.R,
) -> pd.DataFrame | float:
    """Calculate Return.convert."""
    if backend == Backend.R:
        return Rconvert(
            R, destination_type=destination_type, seed_value=seed_value, initial=initial
        )
    raise NotImplementedError(
        f"Backend {backend.value} not implemented for Return.convert"
    )
