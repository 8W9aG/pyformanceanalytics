"""Tests for the OmegaSharpeRatio function."""
import pandas as pd
from pyformanceanalytics import OmegaSharpeRatio


def test_omega_sharpe_ratio():
    df = pd.read_csv("pyformanceanalytics/managers.csv", index_col=0)
    df.index = pd.to_datetime(df.index)
    R = df[["HAM1"]]
    assert OmegaSharpeRatio(R) == 2.1906893464637407
