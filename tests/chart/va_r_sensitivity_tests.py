"""Tests for the VaRSensitivity function."""
import pandas as pd
from pyformanceanalytics.chart import VaRSensitivity


def test_va_r_sensitivity():
    df = pd.read_csv("pyformanceanalytics/managers.csv", index_col=0)
    df.index = pd.to_datetime(df.index)
    assert VaRSensitivity(df) is not None
