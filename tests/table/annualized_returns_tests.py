"""Tests for the AnnualizedReturns function."""
import pandas as pd
from pyformanceanalytics.table import AnnualizedReturns


def test_annualized_returns():
    df = pd.read_csv("pyformanceanalytics/managers.csv", index_col=0)
    df.index = pd.to_datetime(df.index)
    expected_df = pd.DataFrame(data={
        "HAM1": [0.1375, 0.0888, 1.5491],
    }, index=["Annualized Return", "Annualized Std Dev", "Annualized Sharpe (Rf=0%)"])
    R = df[["HAM1"]]
    assert AnnualizedReturns(R).equals(expected_df)
