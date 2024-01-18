"""Tests for the BetaCoVariance function."""
import pandas as pd
from pyformanceanalytics import BetaCoVariance


def test_beta_co_variance():
    df = pd.read_csv("pyformanceanalytics/managers.csv", index_col=0)
    Ra = df[["HAM2"]]
    Rb = df[["SP500 TR"]]
    assert BetaCoVariance(Ra, Rb) == 0.34316210879724557
