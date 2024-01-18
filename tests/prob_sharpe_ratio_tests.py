"""Tests for the ProbSharpeRatio function."""
import pandas as pd
from pyformanceanalytics import ProbSharpeRatio


def test_prob_sharpe_ratio():
    df = pd.read_csv("pyformanceanalytics/managers.csv", index_col=0)
    df.index = pd.to_datetime(df.index)
    expected_df = pd.DataFrame(data={
        "HAM1..SR...0.23..": [0.9871948357133288],
        "sr_confidence_interval.Lower.Bound": [0.2837],
        "sr_confidence_interval.Sharpe.Ratio": [0.434],
        "sr_confidence_interval.Upper.Bound": [0.5843],
    }, index=["Probabilistic Sharpe Ratio(p= 95 %):"])
    R = df[["HAM1"]]
    assert ProbSharpeRatio(0.23, R=R).equals(expected_df)
