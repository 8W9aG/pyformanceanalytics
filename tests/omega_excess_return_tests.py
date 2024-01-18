"""Tests for the OmegaExcessReturn function."""
import pandas as pd
from pyformanceanalytics import OmegaExcessReturn


def test_omega_excess_return():
    df = pd.read_csv("pyformanceanalytics/managers.csv", index_col=0)
    df.index = pd.to_datetime(df.index)
    Ra = df[["HAM1"]]
    Rb = df[["SP500 TR"]]
    assert OmegaExcessReturn(Ra, Rb) == 0.12272677666805255
