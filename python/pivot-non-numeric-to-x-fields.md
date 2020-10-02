```python
import pandas as pd

# sample data
df = pd.DataFrame([[1, 1, 'a'],
                  [1, 1, 'b'],
                  [1, 1, 'c'],
                  [2, 2, 'd'],
                  [2, 2, 'e'],
                  [2, 2, 'f'],
                  [2, 2, 'g'],
                  [2, 2, 'h'],
                  [3, 3, 'a'],
                  [3, 3, 'a']],
                  columns=['npi', 'tin', 'service_location'])

print('Sample data')
print(df.to_markdown(), end='\n\n')

# groupby().cumcount() is like SQL row_number with partitions
# we want each service location to have an arbitrary number ID from 1 to however many services that a key has
key = ['npi', 'tin']
df['rownum'] = df.sort_values(by=key).groupby(key).cumcount()+1
df['rownum'] = 'SL_' + df['rownum'].astype(str)

print('Added rownum col')
print(df.to_markdown(), end='\n\n')

# last step, pivot the data on key level with service location
pivoted = df.pivot(index=key, 
                   columns=['rownum'], 
                   values='service_location')\
            .reset_index()\
            .fillna('')

print('Pivoted')
print(pivoted.to_markdown(), end='\n\n')
```
Sample data
|    |   npi |   tin | service_location   |
|---:|------:|------:|:-------------------|
|  0 |     1 |     1 | a                  |
|  1 |     1 |     1 | b                  |
|  2 |     1 |     1 | c                  |
|  3 |     2 |     2 | d                  |
|  4 |     2 |     2 | e                  |
|  5 |     2 |     2 | f                  |
|  6 |     2 |     2 | g                  |
|  7 |     2 |     2 | h                  |
|  8 |     3 |     3 | a                  |
|  9 |     3 |     3 | a                  |

Added rownum col
|    |   npi |   tin | service_location   | rownum   |
|---:|------:|------:|:-------------------|:---------|
|  0 |     1 |     1 | a                  | SL_1     |
|  1 |     1 |     1 | b                  | SL_2     |
|  2 |     1 |     1 | c                  | SL_3     |
|  3 |     2 |     2 | d                  | SL_1     |
|  4 |     2 |     2 | e                  | SL_2     |
|  5 |     2 |     2 | f                  | SL_3     |
|  6 |     2 |     2 | g                  | SL_4     |
|  7 |     2 |     2 | h                  | SL_5     |
|  8 |     3 |     3 | a                  | SL_1     |
|  9 |     3 |     3 | a                  | SL_2     |

Pivoted
|    |   npi |   tin | SL_1   | SL_2   | SL_3   | SL_4   | SL_5   |
|---:|------:|------:|:-------|:-------|:-------|:-------|:-------|
|  0 |     1 |     1 | a      | b      | c      |        |        |
|  1 |     2 |     2 | d      | e      | f      | g      | h      |
|  2 |     3 |     3 | a      | a      |        |        |        |
