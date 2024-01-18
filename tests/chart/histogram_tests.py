"""Tests for the Histogram function."""
import pandas as pd
from pyformanceanalytics.chart import Histogram


def test_histogram():
    df = pd.read_csv("pyformanceanalytics/managers.csv", index_col=0)
    df.index = pd.to_datetime(df.index)
    assert Histogram(df) is not None
