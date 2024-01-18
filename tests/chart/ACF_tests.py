"""Tests for the ACF function."""
import pandas as pd
from pyformanceanalytics.chart import ACF


def test_ACF():
    df = pd.read_csv("pyformanceanalytics/managers.csv", index_col=0)
    df.index = pd.to_datetime(df.index)
    R = df[["HAM1"]]
    assert ACF(R) is not None
