"""Tests for the UpDownRatios function."""
import pandas as pd
from pyformanceanalytics.table import UpDownRatios

def test_up_down_ratios():
    df = pd.read_csv("pyformanceanalytics/managers.csv", index_col=0)
    df.index = pd.to_datetime(df.index)
    expected_df = pd.DataFrame(data={
        "Up Capture": [0.6347],
        "Down Capture": [0.2076],
        "Up Number": [0.8941],
        "Down Number": [0.5106],
        "Up Percent": [0.2941],
        "Down Percent": [0.8085],
    }, index=["HAM1 to SP500.TR"])
    Ra = df[["HAM1"]]
    Rb = df[["SP500 TR"]]
    assert UpDownRatios(Ra, Rb).equals(expected_df)
