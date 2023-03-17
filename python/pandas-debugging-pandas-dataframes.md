# Debugging Pandas DataFrames inside a method chain

## Problem
* You want to use method chaining with pandas dataframes to avoid repeated assignments. This keeps the code readable in a functional/unix-pipey style.
* But - you still want the option to store a copy of an intermediate dataframe for inspection and debugging.

## Solution
* You can create a function that stores the intermediate dataframe contents under a new variable name. See `store_df_for_debugging`.
* Then later, you have access both to your input, output, and as many intermediate dataframes as you need. 
* Another bonus is that this is easy to comment in and out to save memory when you're done debugging.
* Messing with globals() is admittedly hacky and clutters your namespace. This is a tool for more exploratory, analytical types of work.

```python
import pandas as pd


def store_df_for_debugging(df, df_var_name):
    globals()[df_var_name] = df
    return df


def get_df_var_name(df):
    return [k for k, v in globals().items() if df.equals(v) and k != "df"][-1]


df_in = pd.DataFrame(
    [
        {"item": "apple", "price": 1.0},
        {"item": "banana", "price": 0.5},
    ]
)

df_out = (
  df_in
    .pipe(lambda _df: _df.assign(price=_df["price"] * 2))
    .pipe(store_df_for_debugging, "df_intermediate")
    .pipe(lambda _df: _df.assign(price=_df["price"] * 3))
)

for df in [df_in, df_intermediate, df_out]:
    print(df.pipe(get_df_var_name))
    print(df.to_markdown(index=False))
    print()
```

df_in
| item   |   price |
|:-------|--------:|
| apple  |     1   |
| banana |     0.5 |

df_intermediate
| item   |   price |
|:-------|--------:|
| apple  |       2 |
| banana |       1 |

df_out
| item   |   price |
|:-------|--------:|
| apple  |       6 |
| banana |       3 |
