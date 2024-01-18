"""Tests for the excess function."""
import pandas as pd
from pyformanceanalytics.Return.annualized import excess


def test_excess():
    df = pd.read_csv("pyformanceanalytics/managers.csv", index_col=0)
    df.index = pd.to_datetime(df.index)
    expected_df = pd.DataFrame(data={
        "HAM1": [0.037188834040240426],
    }, index=["Annualized Return"])
    Ra = df[["HAM1"]]
    Rb = df[["SP500 TR"]]
    assert excess(Ra, Rb).equals(expected_df)
