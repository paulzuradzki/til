# Problem

For CLIs in large repos or using larger third-party libraries (ie, Django `python manage.py` and `pandas`), imports are eagerly loaded at runtime. This leads to slow startup times for even basic things like running a `--help` command, because a bunch of unrelated modules are loaded.

ie,

```python
import pandas as pd # slow import on initial load

def transform_df(df: pd.DataFrame) -> pd.DataFrame:
    return df.groupby(["state", "organization"], as_index=False).size()
```

# Solution
One workaround for this is to use "inline imports": move imports within the scope of a function where the library gets used. Then use linting rules to ban module-level imports of the offending libraries.

```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import pandas as pd

def transform_df(df: "pd.DataFrame") -> "pd.DataFrame":
    import pandas as pd # noqa
    return df.groupby(["state", "organization"], as_index=False).size()
```

Python [PEP 810](https://peps.python.org/pep-0810/) ([discussion](https://discuss.python.org/t/pep-810-explicit-lazy-imports/104131)) introduces new syntax to avoid this workaround by explicitly declaring lazy imports like below.

```python
lazy import pandas as pd

def transform_df(df: pd.DataFrame) -> pd.DataFrame:
    return df.groupby(["state", "organization"], as_index=False).size()
```