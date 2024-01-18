"""Tests for the NetSelectivity function."""
import pandas as pd
from pyformanceanalytics import NetSelectivity


def test_net_selectivity():
    df = pd.read_csv("pyformanceanalytics/managers.csv", index_col=0)
    df.index = pd.to_datetime(df.index)
    expected_df = pd.DataFrame(data={
        "HAM1": [0.0802817000429434],
    }, index=["HAM1"])
    Ra = df[["HAM1"]]
    Rb = df[["SP500 TR"]]
    assert NetSelectivity(Ra, Rb).equals(expected_df)
