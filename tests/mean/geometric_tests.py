"""Tests for the geometric function."""
import pandas as pd
from pyformanceanalytics.mean import geometric


def test_geometric():
    df = pd.read_csv("pyformanceanalytics/managers.csv", index_col=0)
    df.index = pd.to_datetime(df.index)
    expected_df = pd.DataFrame(data={
        "HAM1": [0.010796281479811709],
    }, index=["Geometric Mean"])
    R = df[["HAM1"]]
    assert geometric(R).equals(expected_df)
