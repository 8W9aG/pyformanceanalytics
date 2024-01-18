"""Tests for the CaptureRatios function."""
import pandas as pd
from pyformanceanalytics.table import CaptureRatios

def test_capture_ratios():
    df = pd.read_csv("pyformanceanalytics/managers.csv", index_col=0)
    df.index = pd.to_datetime(df.index)
    expected_df = pd.DataFrame(data={
        "Up Capture": [0.6347],
        "Down Capture": [0.2076],
    }, index=["HAM1"])
    Ra = df[["HAM1"]]
    Rb = df[["SP500 TR"]]
    assert CaptureRatios(Ra, Rb).equals(expected_df)
