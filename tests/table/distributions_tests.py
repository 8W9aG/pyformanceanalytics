"""Tests for the Distributions function."""
import pandas as pd
from pyformanceanalytics.table import Distributions

def test_distributions():
    df = pd.read_csv("pyformanceanalytics/managers.csv", index_col=0)
    df.index = pd.to_datetime(df.index)
    expected_df = pd.DataFrame(data={
        "HAM1": [0.0256, -0.6588, 5.3616, 2.3616, -0.6741, 2.5004],
    }, index=["monthly  Std Dev", "Skewness", "Kurtosis", "Excess kurtosis", "Sample skewness", "Sample excess kurtosis"])
    R = df[["HAM1"]]
    assert Distributions(R).equals(expected_df)
