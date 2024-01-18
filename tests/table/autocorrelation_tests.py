"""Tests for the Autocorrelation function."""
import pandas as pd
from pyformanceanalytics.table import Autocorrelation


def test_autocorrelation():
    df = pd.read_csv("pyformanceanalytics/managers.csv", index_col=0)
    df.index = pd.to_datetime(df.index)
    expected_df = pd.DataFrame(data={
        "HAM1": [0.1890, -0.0847, -0.0602, -0.1842, -0.0035, 0.0492, 0.0788],
    }, index=["rho1", "rho2", "rho3", "rho4", "rho5", "rho6", "Q(6) p-value"])
    R = df[["HAM1"]]
    assert Autocorrelation(R).equals(expected_df)
