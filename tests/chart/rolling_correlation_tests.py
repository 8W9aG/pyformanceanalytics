"""Tests for the RollingCorrelation function."""
import pandas as pd
from pyformanceanalytics.chart import RollingCorrelation


def test_rolling_correlation():
    df = pd.read_csv("pyformanceanalytics/managers.csv", index_col=0)
    df.index = pd.to_datetime(df.index)
    Ra = df[["HAM1"]]
    Rb = df[["SP500 TR"]]
    assert RollingCorrelation(Ra, Rb) is not None
