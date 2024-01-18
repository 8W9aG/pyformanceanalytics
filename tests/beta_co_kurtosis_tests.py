"""Tests for the BetaCoKurtosis function."""
import pandas as pd
from pyformanceanalytics import BetaCoKurtosis


def test_beta_co_kurtosis():
    df = pd.read_csv("pyformanceanalytics/managers.csv", index_col=0)
    Ra = df[["HAM2"]]
    Rb = df[["SP500 TR"]]
    assert BetaCoKurtosis(Ra, Rb) == 0.1988372729851128
