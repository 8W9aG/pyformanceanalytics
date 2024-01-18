# pyformanceanalytics.M2

These examples will draw on the following datasets:

```python
import pandas as pd

df = pd.read_csv("pyformanceanalytics/managers.csv", index_col=0)
df.index = pd.to_datetime(df.index)
weights_df = pd.read_csv("pyformanceanalytics/weights.csv", index_col=0)
```

## Functions

The following functions are supported:

### ewma

Calculates exponentially weighted moving average covariance, coskewness and cokurtosis matrices for 2nd degree moments

```python
from pyformanceanalytics.M2 import ewma

R = df[["HAM1"]]
ewma(R)
```

### shrink

Calculates covariance, coskewness and cokurtosis matrices using linear shrinkage between the sample estimator and a structured estimator for 2nd degree moments

```python
from pyformanceanalytics.M2 import shrink

shrink(df[["HAM1", "HAM2"]])
```

### struct

Calculates covariance, coskewness and cokurtosis matrices as structured estimators for 2nd degree moments

```python
from pyformanceanalytics.M2 import struct

struct(df[["HAM1", "HAM2"]])
```
