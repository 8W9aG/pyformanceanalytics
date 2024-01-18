"""Tests for the CaptureRatios function."""
import pandas as pd
from pyformanceanalytics.chart import CaptureRatios


def test_capture_ratios():
    df = pd.read_csv("pyformanceanalytics/managers.csv", index_col=0)
    df.index = pd.to_datetime(df.index)
    Ra = df[["HAM1"]]
    Rb = df[["SP500 TR"]]
    assert CaptureRatios(Ra, Rb) is not None
