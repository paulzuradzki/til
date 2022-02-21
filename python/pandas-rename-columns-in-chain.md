# Problem

Using df.rename() does not work inside method chains if you want to select columns using the new labels further down the chain.

```python
import pandas as pd
import seaborn as sns

df = sns.load_dataset('mpg')
print(df.columns)              # => ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 'acceleration', 'model_year', 'origin', 'name']


# key error
(df 
 .rename({col: col.upper() for col in df.columns})
 .loc[:5, ['NAME', 'MPG']]
)


# key error
(df 
 .pipe(lambda _df: _df.rename({col: col.upper() for col in _df.columns}))
 .loc[:5, ['NAME', 'MPG']]
)
```

# Solution

Use df.set_axis() with axis=1 (or axis='columns')
```python
(df 

 # make column names upper case
 .pipe(lambda _df: _df.set_axis([col.upper() for col in _df.columns], axis='columns'))
 
 # use label-based selection inside chain
 .loc[:5, ['NAME', 'MPG']]
)
```

Or pipe a separate function where columns are re-named via assignment on df.columns like so. However, this does not keep the whole operation inside the chain.
```python
def tweak_df(df):
    df.columns = [col.upper() for col in df.columns]
    return df

(df 
 .pipe(tweak_df)
 .loc[:5, ['NAME', 'MPG']]
)
```
# Output
|    | NAME                      |   MPG |
|---:|:--------------------------|------:|
|  0 | chevrolet chevelle malibu |    18 |
|  1 | buick skylark 320         |    15 |
|  2 | plymouth satellite        |    18 |
|  3 | amc rebel sst             |    16 |
|  4 | ford torino               |    17 |
|  5 | ford galaxie 500          |    15 |
