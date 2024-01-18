"""Tests for the dynamic function."""
import pandas as pd
from pyformanceanalytics.CAPM import dynamic


def test_dynamic():
    df = pd.read_csv("pyformanceanalytics/managers.csv", index_col=0)
    df.index = pd.to_datetime(df.index)
    expected_df = pd.DataFrame(data={
        "Average alpha": [0.009065828586554562],
        "US.10Y.TR alpha at t - 1": [-0.20653992719140177],
        "US.3m.TR alpha at t - 1": [0.35247014053077486],
        "Average beta": [0.32480151039794325],
        "US.10Y.TR beta at t - 1": [3.493336157755593],
        "US.3m.TR beta at t - 1": [-63.74813712124993],
    }, index=["HAM1 to SP500.TR"])
    Ra = df[["HAM1"]]
    Rb = df[["SP500 TR"]]
    Z = df[["US 10Y TR", "US 3m TR"]]
    assert dynamic(Ra, Rb, Z).equals(expected_df)
