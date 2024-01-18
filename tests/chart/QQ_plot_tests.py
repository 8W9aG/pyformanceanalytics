"""Tests for the QQPlot function."""
import pandas as pd
from pyformanceanalytics.chart import QQPlot


def test_QQ_plot():
    df = pd.read_csv("pyformanceanalytics/managers.csv", index_col=0)
    df.index = pd.to_datetime(df.index)
    assert QQPlot(df) is not None
