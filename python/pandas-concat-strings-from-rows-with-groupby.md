### How to concatenate strings from many rows with a group by variable

```python
import pandas as pd

# Set up data. List of lists.
headers = ['member', 'measure1', 'measure2', 'measure3']
data_lol = [[1, 0, 1, 1], [2, 0, 0, 0], [3, 0, 1, 0], [4, 1, 1, 0]]
df = pd.DataFrame(data_lol, columns=headers)
print('df', df.to_markdown(), sep='\n', end='\n\n')

# un-pivot data using melt; filter out member-measures with no values
measure_cols = [col for col in df.columns if 'measure' in col]
melted = pd.melt(df, id_vars=['member'], value_vars=measure_cols, var_name='measure_list', value_name='flag')
melted = melted[melted['flag']==1]
print('melted', melted.to_markdown(), sep='\n', end='\n\n')

# apply string concatenation using GroupBy operation
concat = melted.groupby('member')['measure_list'].apply(lambda row: '; '.join(row)).reset_index()
print('concat', concat.to_markdown(), sep='\n', end='\n\n')

# merge in data with original (use left merge to keep the member without values)
merged = df.merge(concat, on='member', how='left')
merged = merged[['member', 'measure_list']+measure_cols]
print('merged', merged.to_markdown(), sep='\n', end='\n\n')
```

df
|    |   member |   measure1 |   measure2 |   measure3 |
|---:|---------:|-----------:|-----------:|-----------:|
|  0 |        1 |          0 |          1 |          1 |
|  1 |        2 |          0 |          0 |          0 |
|  2 |        3 |          0 |          1 |          0 |
|  3 |        4 |          1 |          1 |          0 |

melted
|    |   member | measure_list   |   flag |
|---:|---------:|:---------------|-------:|
|  3 |        4 | measure1       |      1 |
|  4 |        1 | measure2       |      1 |
|  6 |        3 | measure2       |      1 |
|  7 |        4 | measure2       |      1 |
|  8 |        1 | measure3       |      1 |

concat
|    |   member | measure_list       |
|---:|---------:|:-------------------|
|  0 |        1 | measure2; measure3 |
|  1 |        3 | measure2           |
|  2 |        4 | measure1; measure2 |

merged
|    |   member | measure_list       |   measure1 |   measure2 |   measure3 |
|---:|---------:|:-------------------|-----------:|-----------:|-----------:|
|  0 |        1 | measure2; measure3 |          0 |          1 |          1 |
|  1 |        2 | nan                |          0 |          0 |          0 |
|  2 |        3 | measure2           |          0 |          1 |          0 |
|  3 |        4 | measure1; measure2 |          1 |          1 |          0 |
