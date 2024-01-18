"""Tests for the Stats function."""
import pandas as pd
from pyformanceanalytics.table import Stats


def test_stats():
    df = pd.read_csv("pyformanceanalytics/managers.csv", index_col=0)
    df.index = pd.to_datetime(df.index)
    expected_df = pd.DataFrame(data={
        "HAM1": [132.0, 0.0, -0.0944, 0.0, 0.0112, 0.0111, 0.0108, 0.0248, 0.0692, 0.0022, 0.0067, 0.0155, 0.0007, 0.0256, -0.6588, 2.3616]
    }, index=["Observations", "NAs", "Minimum", "Quartile 1", "Median", "Arithmetic Mean", "Geometric Mean", "Quartile 3", "Maximum", "SE Mean", "LCL Mean (0.95)", "UCL Mean (0.95)", "Variance", "Stdev", "Skewness", "Kurtosis"])
    R = df[["HAM1"]]
    assert Stats(R).equals(expected_df)
