# pyformanceanalytics.Return.annualized

These examples will draw on the following datasets:

```python
import pandas as pd

df = pd.read_csv("pyformanceanalytics/managers.csv", index_col=0)
df.index = pd.to_datetime(df.index)
weights_df = pd.read_csv("pyformanceanalytics/weights.csv", index_col=0)
```

## Functions

The following functions are supported:

### annualized

An average annualized return is convenient for comparing returns

```python
from pyformanceanalytics.Return.annualized import annualized

R = df[["HAM1"]]
annualized(R)
```

### excess

An average annualized excess return is convenient for comparing excess returns

```python
from pyformanceanalytics.Return.annualized import excess

Ra = df[["HAM1"]]
Rb = df[["SP500 TR"]]
excess(Ra, Rb)
```
