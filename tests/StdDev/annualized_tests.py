"""Tests for the annualized function."""
import pandas as pd
from pyformanceanalytics.StdDev import annualized


def test_annualized():
    df = pd.read_csv("pyformanceanalytics/managers.csv", index_col=0)
    df.index = pd.to_datetime(df.index)
    expected_df = pd.DataFrame(data={
        "HAM1": [0.08878079626175704],
    }, index=["Annualized Standard Deviation"])
    R = df[["HAM1"]]
    assert annualized(R).equals(expected_df)
