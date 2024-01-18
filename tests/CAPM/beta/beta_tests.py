"""Tests for the beta function."""
import pandas as pd
from pyformanceanalytics.CAPM.beta import beta


def test_beta():
    df = pd.read_csv("pyformanceanalytics/managers.csv", index_col=0)
    df.index = pd.to_datetime(df.index)
    Ra = df[["HAM1"]]
    Rb = df[["SP500 TR"]]
    assert beta(Ra, Rb) == 0.39060332560510497
