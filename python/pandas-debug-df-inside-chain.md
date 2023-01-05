# Problem

I want to inspect a pandas dataframe during intermediate steps of method chain for debugging.

# Solution
Use pipe() and save intermediate dataframe to global variable for inspection later.

Credit: `save_df_to_var()` function sourced via Matt Harrison, author of Effective Pandas.

```python
import pandas as pd
import seaborn as sns

def save_df_to_var(df, var_name):
    """Debug dataframes inside method chain."""
    globals()[var_name] = df
    return df

iris_df = sns.load_dataset('iris')

grouped_df = (
iris_df
  .groupby(['species'])
  .mean()
  .pipe(save_df_to_var, 'df_debug_1')
  .reset_index()
  .pipe(save_df_to_var, 'df_debug_2')
)
```

# Discussion

* The advantage of this approach is that you do not have to re-write the method chain and create new assignments outside the chain. 
* The pipe() line is easy to include or comment out.
