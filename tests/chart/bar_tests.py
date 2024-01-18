"""Tests for the Bar function."""
import pandas as pd
from pyformanceanalytics.chart import Bar


def test_bar():
    df = pd.read_csv("pyformanceanalytics/managers.csv", index_col=0)
    df.index = pd.to_datetime(df.index)
    R = df[["HAM1"]]
    assert Bar(R) is not None
