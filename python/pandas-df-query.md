```python
# df.query() can be used in place boolean indexing for more concise code
# if you prefer not to re-reference the source dataframe
# dataf


values_df = pd.DataFrame([[15.0], [24.0], [1.0], [98.0], [48.0], [97.0], [29.0], [86.0], [27.0], [59.0]], columns=['values'])
# equivalent:
values_df_filtered = values_df[values_df['values']>=40]
values_df_filtered = values_df.query('values >= 40')


states_df = pd.DataFrame([['CALIFORNIA', 'CA'], ['FLORIDA', 'FL'], ['ILLINOIS', 'IL'], ['INDIANA', 'IN'], 
                          ['WISCONSIN', 'WI'], ['WYOMING', 'WY']],
            columns=['state', 'abbr'])
# equivalent:
states_filtered = states_df.query("abbr.str.contains('IL')")
states_filtered = states_df[states_df['abbr'].str.contains('IL')]
```

values_df
|    |   values |
|---:|---------:|
|  0 |       15 |
|  1 |       24 |
|  2 |        1 |
|  3 |       98 |
|  4 |       48 |
|  5 |       97 |
|  6 |       29 |
|  7 |       86 |
|  8 |       27 |
|  9 |       59 |

values_filtered
|    |   values |
|---:|---------:|
|  3 |       98 |
|  4 |       48 |
|  5 |       97 |
|  7 |       86 |
|  9 |       59 |

states_df
|    | state      | abbr   |
|---:|:-----------|:-------|
|  0 | CALIFORNIA | CA     |
|  1 | FLORIDA    | FL     |
|  2 | ILLINOIS   | IL     |
|  3 | INDIANA    | IN     |
|  4 | WISCONSIN  | WI     |
|  5 | WYOMING    | WY     |

states_filtered
|    | state    | abbr   |
|---:|:---------|:-------|
|  2 | ILLINOIS | IL     |
|  3 | INDIANA  | IN     |
