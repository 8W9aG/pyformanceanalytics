# pyformanceanalytics.SharpeRatio

These examples will draw on the following datasets:

```python
import pandas as pd

df = pd.read_csv("pyformanceanalytics/managers.csv", index_col=0)
df.index = pd.to_datetime(df.index)
weights_df = pd.read_csv("pyformanceanalytics/weights.csv", index_col=0)
```

## Functions

The following functions are supported:

### SharpeRatio

The Sharpe ratio is simply the return per unit of risk (represented by variability)

```python
from pyformanceanalytics.SharpeRatio import SharpeRatio

R = df[["HAM1"]]
SharpeRatio(R)
```

### modified

Calculates the modified sharpe ratio

```python
from pyformanceanalytics.SharpeRatio import modified

R = df[["HAM1"]]
modified(R)
```

### annualized

Calculates the annualized sharpe ratio

```python
from pyformanceanalytics.SharpeRatio import annualized

R = df[["HAM1"]]
annualized(R)
```
