"""Tests for the ProbOutPerformance function."""
import pandas as pd
from pyformanceanalytics.table import ProbOutPerformance


def test_prob_out_performance():
    df = pd.read_csv("pyformanceanalytics/managers.csv", index_col=0)
    df.index = pd.to_datetime(df.index)
    expected_df = pd.DataFrame(data={
        "period_lengths": [1, 3, 6, 9, 12, 18, 36],
        "HAM1": [63.0, 70.0, 67.0, 67.0, 72.0, 74.0, 73.0],
        "SP500.TR": [68.0, 60.0, 60.0, 57.0, 49.0, 41.0, 24.0],
        "total periods": [131.0, 130.0, 127.0, 124.0, 121.0, 115.0, 97.0],
        "prob_HAM1_outperformance": [0.48091603053435117, 0.5384615384615384, 0.5275590551181102, 0.5403225806451613, 0.5950413223140496, 0.6434782608695652, 0.7525773195876289],
        "prob_SP500.TR_outperformance": [0.5190839694656488, 0.46153846153846156, 0.47244094488188976, 0.4596774193548387, 0.4049586776859504, 0.3565217391304348, 0.24742268041237114],
    }, index=[1, 2, 3, 4, 5, 6, 7])
    Ra = df[["HAM1"]]
    Rb = df[["SP500 TR"]]
    assert ProbOutPerformance(Ra, Rb).to_csv() == expected_df.to_csv()
