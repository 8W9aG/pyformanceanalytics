"""Tests for the AdjustedSharpeRatio function."""
import pandas as pd
from pyformanceanalytics import AppraisalRatio


def test_appraisal_ratio():
    df = pd.read_csv("pyformanceanalytics/managers.csv", index_col=0)
    df.index = pd.to_datetime(df.index)
    df = df[df.index.year == 1996]
    Ra = df[["HAM1"]]
    Rb = df[["SP500 TR"]]
    assert AppraisalRatio(Ra, Rb) == 1.6230250991956883
