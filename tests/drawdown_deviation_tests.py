"""Tests for the DrawdownDeviation function."""
import pandas as pd
from pyformanceanalytics import DrawdownDeviation


def test_drawdown_deviation():
    df = pd.read_csv("pyformanceanalytics/managers.csv", index_col=0)
    df.index = pd.to_datetime(df.index)
    expected_df = pd.DataFrame(data={
        "HAM1": [0.0182784379335125],
    }, index=["Drawdown Deviation"])
    R = df[["HAM1"]]
    assert DrawdownDeviation(R).equals(expected_df)
