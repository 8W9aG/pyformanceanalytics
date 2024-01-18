"""Tests for the CalendarReturns function."""
import pandas as pd
from pyformanceanalytics.table import CalendarReturns


def test_calendar_returns():
    df = pd.read_csv("pyformanceanalytics/managers.csv", index_col=0)
    df.index = pd.to_datetime(df.index)
    df = df[df.index.year == 1996]
    expected_df = pd.DataFrame(data={
        "Jan": [0.7],
        "Feb": [1.9],
        "Mar": [1.6],
        "Apr": [-0.9],
        "May": [0.8],
        "Jun": [-0.4],
        "Jul": [-2.3],
        "Aug": [4.0],
        "Sep": [1.5],
        "Oct": [2.9],
        "Nov": [1.6],
        "Dec": [1.8],
        "HAM1": [13.6],
    }, index=["1996"])
    R = df[["HAM1"]]
    assert CalendarReturns(R).equals(expected_df)
