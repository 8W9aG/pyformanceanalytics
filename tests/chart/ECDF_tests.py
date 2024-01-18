"""Tests for the ECDF function."""
import pandas as pd
from pyformanceanalytics.chart import ECDF


def test_ECDF():
    df = pd.read_csv("pyformanceanalytics/managers.csv", index_col=0)
    df.index = pd.to_datetime(df.index)
    assert ECDF(df) is not None
