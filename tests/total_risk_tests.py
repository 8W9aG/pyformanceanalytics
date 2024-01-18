"""Tests for the TotalRisk function."""
import pandas as pd
from pyformanceanalytics import TotalRisk


def test_total_risk():
    df = pd.read_csv("pyformanceanalytics/managers.csv", index_col=0)
    df.index = pd.to_datetime(df.index)
    Ra = df[["HAM1"]]
    Rb = df[["SP500 TR"]]
    assert TotalRisk(Ra, Rb) == 0.08859082021982835
