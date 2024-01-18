"""Tests for the BetaCoSkewness function."""
import pandas as pd
from pyformanceanalytics import BetaCoSkewness


def test_beta_co_skewness():
    df = pd.read_csv("pyformanceanalytics/managers.csv", index_col=0)
    Ra = df[["HAM2"]]
    Rb = df[["SP500 TR"]]
    assert BetaCoSkewness(Ra, Rb) == 0.04542926998885854
