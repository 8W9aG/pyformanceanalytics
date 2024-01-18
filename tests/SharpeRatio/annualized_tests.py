"""Tests for the annualized function."""
import pandas as pd
from pyformanceanalytics.SharpeRatio import annualized


def test_annualized():
    df = pd.read_csv("pyformanceanalytics/managers.csv", index_col=0)
    df.index = pd.to_datetime(df.index)
    expected_df = pd.DataFrame(data={
        "HAM1": [1.5491189155161194],
    }, index=["Annualized Sharpe Ratio (Rf=0%)"])
    R = df[["HAM1"]]
    assert annualized(R).equals(expected_df)
