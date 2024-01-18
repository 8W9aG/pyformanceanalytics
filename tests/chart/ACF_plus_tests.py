"""Tests for the ACFplus function."""
import pandas as pd
from pyformanceanalytics.chart import ACFplus


def test_ACF_plus():
    df = pd.read_csv("pyformanceanalytics/managers.csv", index_col=0)
    df.index = pd.to_datetime(df.index)
    R = df[["HAM1"]]
    assert ACFplus(R) is not None
