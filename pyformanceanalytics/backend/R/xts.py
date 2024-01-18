"""Functions for representing a dataframe as an XTS object in R."""
from typing import Any

import pandas as pd
from rpy2 import robjects

from .rimports import utils


def xts_from_df(df: pd.DataFrame) -> Any:
    """Produce an R xts from a python pandas dataframe."""
    csv_var = utils().read_csv.rcall(
        (
            ("text", df.to_csv()),
            ("row.names", 1),
        ),
    )
    return robjects.r("as.xts").rcall(  # type: ignore
        (("x", csv_var),),
    )
