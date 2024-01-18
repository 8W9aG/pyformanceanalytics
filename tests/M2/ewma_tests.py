"""Tests for the ewma function."""
import pandas as pd
from pyformanceanalytics.M2 import ewma


def test_ewma():
    df = pd.read_csv("pyformanceanalytics/managers.csv", index_col=0)
    df.index = pd.to_datetime(df.index)
    df = df[df.index.year == 1996]
    expected_df = pd.DataFrame(data={
        "HAM1": [0.0003903582055034173],
    }, index=["HAM1"])
    R = df[["HAM1"]]
    assert ewma(R).equals(expected_df)
