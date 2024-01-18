"""Tests for the StackedBar function."""
import pandas as pd
from pyformanceanalytics.chart import StackedBar


def test_stacked_bar():
    weights_df = pd.read_csv("pyformanceanalytics/weights.csv", index_col=0)
    assert StackedBar(weights_df) is not None
