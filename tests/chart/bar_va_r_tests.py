"""Tests for the BarVaR function."""
import pandas as pd
from pyformanceanalytics.chart import BarVaR


def test_bar_va_r():
    df = pd.read_csv("pyformanceanalytics/managers.csv", index_col=0)
    df.index = pd.to_datetime(df.index)
    R = df[["HAM1"]]
    assert BarVaR(R) is not None
