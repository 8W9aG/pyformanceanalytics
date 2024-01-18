"""Tests for the RiskPremium function."""
import pandas as pd
from pyformanceanalytics.CAPM import RiskPremium


def test_risk_premium():
    df = pd.read_csv("pyformanceanalytics/managers.csv", index_col=0)
    df.index = pd.to_datetime(df.index)
    expected_df = pd.DataFrame(data={
        "SP500.TR": [0.008665340909090907],
    }, index=["Risk Premium (Rf=0%)"])
    R = df[["SP500 TR"]]
    assert RiskPremium(R).equals(expected_df)
