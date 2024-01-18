"""Tests for the SkewnessKurtosisRatio function."""
import pandas as pd
from pyformanceanalytics import SkewnessKurtosisRatio


def test_skewness_kurtosis_ratio():
    df = pd.read_csv("pyformanceanalytics/managers.csv", index_col=0)
    df.index = pd.to_datetime(df.index)
    R = df[["HAM1"]]
    assert SkewnessKurtosisRatio(R) == -0.12288232480989136
