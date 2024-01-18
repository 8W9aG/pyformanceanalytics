"""Tests for the RollingPerformance function."""
import pandas as pd
from pyformanceanalytics.chart import RollingPerformance


def test_rolling_performance():
    df = pd.read_csv("pyformanceanalytics/managers.csv", index_col=0)
    df.index = pd.to_datetime(df.index)
    assert RollingPerformance(df) is not None
