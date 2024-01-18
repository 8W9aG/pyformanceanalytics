"""The PerformanceAnalytics sortDrawdowns function."""
import pandas as pd


def sortDrawdowns(runs: pd.DataFrame) -> pd.DataFrame:
    """Calculate sortDrawdowns."""
    return runs.sort_values(by=["return"])
