"""Tests for the RollingPeriods function."""
import pandas as pd
from pyformanceanalytics.table import RollingPeriods


def test_rolling_periods():
    df = pd.read_csv("pyformanceanalytics/managers.csv", index_col=0)
    df.index = pd.to_datetime(df.index)
    expected_df = pd.DataFrame(data={
        "HAM1": [0.0160, 0.0114, 0.0092, 0.0258, 0.0202, 0.0273]
    }, index=["Last 12 month Correlation", "Last 36 month Correlation", "Last 60 month Correlation", "Last 12 month Beta", "Last 36 month Beta", "Last 60 month Beta"])
    R = df[["HAM1"]]
    assert RollingPeriods(R).equals(expected_df)
