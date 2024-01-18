"""Tests for the CumReturns function."""
import pandas as pd
from pyformanceanalytics.chart import CumReturns


def test_cum_returns():
    df = pd.read_csv("pyformanceanalytics/managers.csv", index_col=0)
    df.index = pd.to_datetime(df.index)
    assert CumReturns(df) is not None
