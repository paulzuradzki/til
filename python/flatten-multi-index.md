# Remove multi-index example
![Remove multi-index example](https://pbpython.com/images/column_flatten.png)

```python

# source: https://pbpython.com/groupby-agg.html
# by Chris Moffett

multi_df = df.groupby(['embark_town', 'class'],
                    as_index=False).agg({'fare': ['sum', 'mean']})

multi_df.columns = [
'_'.join(col).rstrip('_') for col in multi_df.columns.values
]

```


