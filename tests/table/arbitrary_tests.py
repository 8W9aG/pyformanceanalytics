"""Tests for the Arbitrary function."""
import pandas as pd
from pyformanceanalytics.table import Arbitrary


def test_arbitrary():
    df = pd.read_csv("pyformanceanalytics/managers.csv", index_col=0)
    df.index = pd.to_datetime(df.index)
    expected_df = pd.DataFrame(data={
        "HAM1": [0.011122727272727272, 0.025628808310297378],
    }, index=["Average Return", "Standard Deviation"])
    R = df[["HAM1"]]
    assert Arbitrary(R).equals(expected_df)
