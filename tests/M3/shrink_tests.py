"""Tests for the shrink function."""
import pandas as pd
from pyformanceanalytics.M3 import shrink


def test_shrink():
    df = pd.read_csv("pyformanceanalytics/managers.csv", index_col=0)
    df.index = pd.to_datetime(df.index)
    expected_df = pd.DataFrame(data={
        "M3sh.1": [None, None],
        "M3sh.2": [None, None],
        "M3sh.3": [None, None],
        "M3sh.4": [None, None],
        "lambda": [None, None],
        "A": [None, None],
        "b": [None, None],
    }, index=[1, 2])
    R = df[["HAM1", "HAM2"]]
    assert shrink(R).to_csv() == expected_df.to_csv()
