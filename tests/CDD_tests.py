"""Tests for the CDD function."""
import pandas as pd
from pyformanceanalytics import CDD


def test_CDD():
    df = pd.read_csv("pyformanceanalytics/managers.csv", index_col=0)
    df.index = pd.to_datetime(df.index)
    expected_df = pd.DataFrame(data={
        "HAM1": [0.08251643884224796],
        "HAM2": [0.06240640733414787],
        "HAM3": [0.07097734399999996],
        "HAM4": [0.2758856510591589],
        "HAM5": [0.28302333322177714],
        "HAM6": [0.07134841429875687],
        "EDHEC.LS.EQ": [0.04919200099680005],
        "SP500.TR": [0.1365640359999999],
        "US.10Y.TR": [0.0757935323412192],
        "US.3m.TR": [0.0],
    }, index=["Conditional Drawdown 5%"])
    assert CDD(df).equals(expected_df)
