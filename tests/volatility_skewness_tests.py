"""Tests for the VolatilitySkewness function."""
import pandas as pd
from pyformanceanalytics import VolatilitySkewness


def test_volatility_skewness():
    df = pd.read_csv("pyformanceanalytics/managers.csv", index_col=0)
    df.index = pd.to_datetime(df.index)
    R = df[["HAM1"]]
    assert VolatilitySkewness(R) == 2.6681610300788416
