"""Tests for the SpecificRisk function."""
import pandas as pd
from pyformanceanalytics.table import SpecificRisk


def test_specific_risk():
    df = pd.read_csv("pyformanceanalytics/managers.csv", index_col=0)
    df.index = pd.to_datetime(df.index)
    expected_df = pd.DataFrame(data={
        "HAM1": [0.0664, 0.0586, 0.0886]
    }, index=["Specific Risk", "Systematic Risk", "Total Risk"])
    Ra = df[["HAM1"]]
    Rb = df[["SP500 TR"]]
    assert SpecificRisk(Ra, Rb).equals(expected_df)
