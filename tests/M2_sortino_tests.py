"""Tests for the M2Sortino function."""
import pandas as pd
from pyformanceanalytics import M2Sortino


def test_M2_sortino():
    df = pd.read_csv("pyformanceanalytics/managers.csv", index_col=0)
    df.index = pd.to_datetime(df.index)
    df = df[df.index.year == 1996]
    expected_df = pd.DataFrame(data={
        "HAM1": [0.1709468424074905],
    }, index=["Sortino Ratio (MAR = 0%)"])
    Ra = df[["HAM1"]]
    Rb = df[["SP500 TR"]]
    assert M2Sortino(Ra, Rb, 0.0).equals(expected_df)
