"""Tests for the SharpeRatio function."""
import pandas as pd
from pyformanceanalytics.SharpeRatio import SharpeRatio


def test_sharpe_ratio():
    df = pd.read_csv("pyformanceanalytics/managers.csv", index_col=0)
    df.index = pd.to_datetime(df.index)
    expected_df = pd.DataFrame(data={
        "HAM1": [0.43399315091284524],
    }, index=["StdDev Sharpe (Rf=0%, p=95%):"])
    R = df[["HAM1"]]
    assert SharpeRatio(R).equals(expected_df)
