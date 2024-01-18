"""Tests for the RollingMean function."""
import pandas as pd
from pyformanceanalytics.chart import RollingMean


def test_rolling_mean():
    df = pd.read_csv("pyformanceanalytics/managers.csv", index_col=0)
    df.index = pd.to_datetime(df.index)
    assert RollingMean(df) is not None
