"""Tests for the PerformanceSummary function."""
import pandas as pd
from pyformanceanalytics.charts import PerformanceSummary


def test_performance_summary():
    df = pd.read_csv("pyformanceanalytics/managers.csv", index_col=0)
    df.index = pd.to_datetime(df.index)
    assert PerformanceSummary(df) is not None
