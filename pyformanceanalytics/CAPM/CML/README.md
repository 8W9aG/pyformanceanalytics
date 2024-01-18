# pyformanceanalytics.CAPM.CML

These examples will draw on the following datasets:

```python
import pandas as pd

df = pd.read_csv("pyformanceanalytics/managers.csv", index_col=0)
df.index = pd.to_datetime(df.index)
weights_df = pd.read_csv("pyformanceanalytics/weights.csv", index_col=0)
```

## Functions

The following functions are supported:

### slope

The slope of the CML is the Sharpe Ratio for the market portfolio.

```python
from pyformanceanalytics.CAPM.CML import slope

R = df[["SP500 TR"]]
slope(R)
```

### CML

The Capital Market Line for the portfolio

```python
from pyformanceanalytics.CAPM.CML import CML

Ra = df[["HAM1"]]
Rb = df[["SP500 TR"]]
CML(Ra, Rb)
```
