"""Tests for the AdjustedSharpeRatio function."""
import pandas as pd
from pyformanceanalytics import AdjustedSharpeRatio


def test_adjusted_sharpe_ratio():
    df = pd.read_csv("pyformanceanalytics/managers.csv", index_col=0)
    df.index = pd.to_datetime(df.index)
    df = df[df.index.year == 1996]
    expected_df = pd.DataFrame(data={
        "HAM1": [2.0459678581282934],
        "HAM2": [14.559302953100614],
        "HAM3": [0.9322735623588032],
        "HAM4": [1.8833683126852616],
        "HAM5": [float('nan')],
        "HAM6": [float('nan')],
        "EDHEC.LS.EQ": [float('nan')],
        "SP500.TR": [1.9869615711208082],
        "US.10Y.TR": [0.006312774451578858],
        "US.3m.TR": [-576.9696274528212],
    }, index=["Adjusted Sharpe ratio (Risk free = 0)"])
    assert AdjustedSharpeRatio(df).equals(expected_df)
