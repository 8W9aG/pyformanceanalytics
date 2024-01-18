"""Tests for the RelativePerformance function."""
import pandas as pd
from pyformanceanalytics.chart import RelativePerformance


def test_relative_performance():
    df = pd.read_csv("pyformanceanalytics/managers.csv", index_col=0)
    df.index = pd.to_datetime(df.index)
    Ra = df[["HAM1"]]
    Rb = df[["SP500 TR"]]
    assert RelativePerformance(Ra, Rb) is not None
