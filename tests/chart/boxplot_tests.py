"""Tests for the Boxplot function."""
import pandas as pd
from pyformanceanalytics.chart import Boxplot


def test_box_plot():
    df = pd.read_csv("pyformanceanalytics/managers.csv", index_col=0)
    df.index = pd.to_datetime(df.index)
    R = df[["HAM1"]]
    assert Boxplot(R) is not None
