"""Tests for the ActivePremium function."""
import pandas as pd
from pyformanceanalytics import ActivePremium


def test_active_premium():
    df = pd.read_csv("pyformanceanalytics/managers.csv", index_col=0)
    Ra = df[["HAM1"]]
    Rb = df[["SP500 TR"]]
    assert ActivePremium(Ra, Rb) == 0.04078668008909658
