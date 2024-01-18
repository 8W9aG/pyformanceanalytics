"""Tests for the shrink function."""
import pandas as pd
from pyformanceanalytics.M4 import shrink


def test_shrink():
    df = pd.read_csv("pyformanceanalytics/managers.csv", index_col=0)
    df.index = pd.to_datetime(df.index)
    expected_df = pd.DataFrame(data={
        "M4sh.1": [None, None],
        "M4sh.2": [None, None],
        "M4sh.3": [None, None],
        "M4sh.4": [None, None],
        "M4sh.5": [None, None],
        "M4sh.6": [None, None],
        "M4sh.7": [None, None],
        "M4sh.8": [None, None],
        "lambda": [None, None],
        "A": [None, None],
        "b": [None, None],
    }, index=[1, 2])
    R = df[["HAM1", "HAM2"]]
    assert shrink(R).to_csv() == expected_df.to_csv()
