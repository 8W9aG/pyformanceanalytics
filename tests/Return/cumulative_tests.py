"""Tests for the cumulative function."""
import pandas as pd
from pyformanceanalytics.Return import cumulative


def test_cumulative():
    df = pd.read_csv("pyformanceanalytics/managers.csv", index_col=0)
    df.index = pd.to_datetime(df.index)
    expected_df = pd.DataFrame(data={
        "HAM1": [3.1266714641119693],
    }, index=["Cumulative Return"])
    R = df[["HAM1"]]
    assert cumulative(R).equals(expected_df)
