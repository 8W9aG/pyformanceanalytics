"""Tests for the MSquaredExcess function."""
import pandas as pd
from pyformanceanalytics import MSquaredExcess


def test_m_squared_excess():
    df = pd.read_csv("pyformanceanalytics/managers.csv", index_col=0)
    df.index = pd.to_datetime(df.index)
    expected_df = pd.DataFrame(data={
        "SP500.TR": [0.1236980722414418],
    }, index=["SP500.TR"])
    Ra = df[["HAM1"]]
    Rb = df[["SP500 TR"]]
    assert MSquaredExcess(Ra, Rb).equals(expected_df)
