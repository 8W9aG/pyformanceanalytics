"""Tests for the RiskReturnScatter function."""
import pandas as pd
from pyformanceanalytics.chart import RiskReturnScatter


def test_risk_return_scatter():
    df = pd.read_csv("pyformanceanalytics/managers.csv", index_col=0)
    df.index = pd.to_datetime(df.index)
    assert RiskReturnScatter(df) is not None
