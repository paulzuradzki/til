# Problem

* I want to use pandas.Series.value_counts() or pandas.DataFrame.groupby([a_col]).size() to get frequency counts; but I also want the percentages in one go.
* pandas.Series.value_counts() has a normalize=True option for percentages; I want this to be neatly merged with the counts with clear column labels.

# Solution
* method chain with concatenation of 2 series to combine the 2 value counts (counts and percents)
* rename axis and set_axis to adjust new column names inside the chain
* pipe with lambdas to re-format counts (comma separator) and percents (from a decimal to percent)
* TODO: make a groupby version of this to support multiple groupings with a similar count and percent column output

```python
import pandas as pd
import seaborn as sns

def value_counts_with_percent(a_series):
    counts_df = (    
        pd.concat([a_series.value_counts(dropna=False),
                   a_series.value_counts(dropna=False, normalize=True)
                  ]
                  , axis='columns'
                 ) # end concat
        .rename_axis(a_series.name)
        .set_axis(['count', 'pct'], axis='columns')    
        .pipe(lambda _df: _df.assign(count=_df['count'].apply(lambda s: '{:,}'.format(s)),
                                     pct=_df['pct'].apply(lambda s: '{:.2f}%'.format(s*100)),
                                    ) # end assign
             ) # end pipe
        .reset_index()
    )

    return counts_df

df = sns.load_dataset('mpg')

print(df['name'].pipe(value_counts_with_percent)[:10].to_markdown())
print()
print(df['origin'].pipe(value_counts_with_percent)[:10].to_markdown())
```

# Output

|    | name               |   count | pct   |
|---:|:-------------------|--------:|:------|
|  0 | ford pinto         |       6 | 1.51% |
|  1 | toyota corolla     |       5 | 1.26% |
|  2 | amc matador        |       5 | 1.26% |
|  3 | ford maverick      |       5 | 1.26% |
|  4 | chevrolet chevette |       4 | 1.01% |
|  5 | amc gremlin        |       4 | 1.01% |
|  6 | chevrolet impala   |       4 | 1.01% |
|  7 | peugeot 504        |       4 | 1.01% |
|  8 | amc hornet         |       4 | 1.01% |
|  9 | toyota corona      |       4 | 1.01% |

|    | origin   |   count | pct    |
|---:|:---------|--------:|:-------|
|  0 | usa      |     249 | 62.56% |
|  1 | japan    |      79 | 19.85% |
|  2 | europe   |      70 | 17.59% |
