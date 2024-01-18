"""Tests for the Correlation function."""
import pandas as pd
from pyformanceanalytics.chart import Correlation


def test_correlation():
    df = pd.read_csv("pyformanceanalytics/managers.csv", index_col=0)
    df.index = pd.to_datetime(df.index)
    assert Correlation(df) is not None
