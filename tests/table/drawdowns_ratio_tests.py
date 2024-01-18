"""Tests for the DrawdownsRatio function."""
import pandas as pd
from pyformanceanalytics.table import DrawdownsRatio


def test_drawdowns_ratio():
    df = pd.read_csv("pyformanceanalytics/managers.csv", index_col=0)
    df.index = pd.to_datetime(df.index)
    expected_df = pd.DataFrame(data={
        "HAM1": [0.5463, 0.9062, 0.6593, 0.0157, 0.0362, 8.7789, 3.7992],
    }, index=["Sterling ratio", "Calmar ratio", "Burke ratio", "Pain index", "Ulcer index", "Pain ratio", "Martin ratio"])
    R = df[["HAM1"]]
    assert DrawdownsRatio(R).equals(expected_df)
