"""Tests for the shrink function."""
import pandas as pd
from pyformanceanalytics.M2 import shrink


def test_shrink():
    df = pd.read_csv("pyformanceanalytics/managers.csv", index_col=0)
    df.index = pd.to_datetime(df.index)
    df = df[df.index.year == 1996]
    expected_df = pd.DataFrame(data={
        "M2sh.HAM1": [None, None],
        "M2sh.HAM2": [None, None],
        "lambda": [None, None],
        "A": [None, None],
        "b": [None, None],
    }, index=["HAM1", "HAM2"])
    R = df[["HAM1", "HAM2"]]
    assert shrink(R).to_csv() == expected_df.to_csv()
