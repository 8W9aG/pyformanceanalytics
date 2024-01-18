"""Tests for the RollingQuantileRegression function."""
import pandas as pd
from pyformanceanalytics.chart import RollingQuantileRegression


def test_rolling_quantile_regression():
    df = pd.read_csv("pyformanceanalytics/managers.csv", index_col=0)
    df.index = pd.to_datetime(df.index)
    Ra = df[["HAM1"]]
    Rb = df[["SP500 TR"]]
    assert RollingQuantileRegression(Ra, Rb) is not None
