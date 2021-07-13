```python
import pandas as pd

data = [
 {'memberid': 'a', 'hcc': 'hcc_1'},
 {'memberid': 'a', 'hcc': 'hcc_1'},
 {'memberid': 'a', 'hcc': 'hcc_1'},
 {'memberid': 'a', 'hcc': 'hcc_8'},
 {'memberid': 'a', 'hcc': 'hcc_3'},
 {'memberid': 'b', 'hcc': 'hcc_3'},
 {'memberid': 'b', 'hcc': 'hcc_9'},
 {'memberid': 'c', 'hcc': 'hcc_1'},
 {'memberid': 'c', 'hcc': 'hcc_2'},
 {'memberid': 'c', 'hcc': 'hcc_3'},
 {'memberid': 'c', 'hcc': 'hcc_4'},
 {'memberid': 'c', 'hcc': 'hcc_5'},
 {'memberid': 'c', 'hcc': 'hcc_6'}]

df = pd.DataFrame(data)

# pivot columns to rows by member aggregating count of HCC
# fill blanks with '' empty string
# if value is not None/empty (if x), then return 1; ensures value of 1 or blank if there are duplicates (count>1) 
df_pivoted = (df.pivot_table(index=['memberid'], columns=['hcc'], values=['hcc'], aggfunc={'hcc': 'size'})
                .fillna('')
                .applymap(lambda x: 1 if x else '')
             )

# fix column formatting in multi-index
df_pivoted.columns = [c for _, c in df_pivoted.columns.values]
df_pivoted = df_pivoted.reset_index()

```

df
|    | memberid   | hcc   |
|---:|:-----------|:------|
|  0 | a          | hcc_1 |
|  1 | a          | hcc_1 |
|  2 | a          | hcc_1 |
|  3 | a          | hcc_8 |
|  4 | a          | hcc_3 |
|  5 | b          | hcc_3 |
|  6 | b          | hcc_9 |
|  7 | c          | hcc_1 |
|  8 | c          | hcc_2 |
|  9 | c          | hcc_3 |
| 10 | c          | hcc_4 |
| 11 | c          | hcc_5 |
| 12 | c          | hcc_6 |

df_pivoted
|    | memberid   | hcc_1   | hcc_2   |   hcc_3 | hcc_4   | hcc_5   | hcc_6   | hcc_8   | hcc_9   |
|---:|:-----------|:--------|:--------|--------:|:--------|:--------|:--------|:--------|:--------|
|  0 | a          | 1       |         |       1 |         |         |         | 1       |         |
|  1 | b          |         |         |       1 |         |         |         |         | 1       |
|  2 | c          | 1       | 1       |       1 | 1       | 1       | 1       |         |         |
