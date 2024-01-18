"""Tests for the UpDownRatios function."""
import pandas as pd
from pyformanceanalytics import UpDownRatios


def test_up_down_ratios():
    df = pd.read_csv("pyformanceanalytics/managers.csv", index_col=0)
    df.index = pd.to_datetime(df.index)
    expected_df = pd.DataFrame(data={
        "0.634661226019341": [0.6346612260193407],
    }, index=[1])
    Ra = df[["HAM1"]]
    Rb = df[["SP500 TR"]]
    assert UpDownRatios(Ra, Rb).to_csv() == expected_df.to_csv()
