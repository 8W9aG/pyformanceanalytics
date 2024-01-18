"""Tests for the TrackingError function."""
import pandas as pd
from pyformanceanalytics import TrackingError


def test_total_risk():
    df = pd.read_csv("pyformanceanalytics/managers.csv", index_col=0)
    df.index = pd.to_datetime(df.index)
    Ra = df[["HAM1"]]
    Rb = df[["SP500 TR"]]
    assert TrackingError(Ra, Rb) == 0.11316665937003545
