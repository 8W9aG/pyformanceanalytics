"""Tests for the MSquared function."""
import pandas as pd
from pyformanceanalytics import MSquared


def test_m_squared():
    df = pd.read_csv("pyformanceanalytics/managers.csv", index_col=0)
    df.index = pd.to_datetime(df.index)
    expected_df = pd.DataFrame(data={
        "SP500.TR": [0.23241061388624332],
    }, index=["SP500.TR"])
    Ra = df[["HAM1"]]
    Rb = df[["SP500 TR"]]
    assert MSquared(Ra, Rb).equals(expected_df)
