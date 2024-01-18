# pyformanceanalytics.CAPM.beta

These examples will draw on the following datasets:

```python
import pandas as pd

df = pd.read_csv("pyformanceanalytics/managers.csv", index_col=0)
df.index = pd.to_datetime(df.index)
weights_df = pd.read_csv("pyformanceanalytics/weights.csv", index_col=0)
```

## Functions

The following functions are supported:

### beta

Calculate single factor model (CAPM) beta.

```python
from pyformanceanalytics.CAPM.beta import beta

Ra = df[["HAM1"]]
Rb = df[["SP500 TR"]]
beta(Ra, Rb)
```

### bull

Calculate single factor model (CAPM) bull beta.

```python
from pyformanceanalytics.CAPM.beta import bull

Ra = df[["HAM1"]]
Rb = df[["SP500 TR"]]
bull(Ra, Rb)
```

### bear

Calculate single factor model (CAPM) bear beta.

```python
from pyformanceanalytics.CAPM.beta import bear

Ra = df[["HAM1"]]
Rb = df[["SP500 TR"]]
bear(Ra, Rb)
```
