### Issue
I want to summarize the distribution of values in a data set for a given column. 
* These values may be categorical or numeric with high cardinality (many distinct values). 
* I want the top 10 values and everything else to go into an "other" bucket. 
* Then I want to combine the frequency counts and percentages.
* I want a utility function so I can apply this to each column in a data set.
* Possible modifications: add parameters to detect or specify data type, toggle "top-N vs Other" behavior

```python
import pandas as pd

def get_col_stats(df, col):
    """Get distribution for categorical column values.
    
    Example
    -------
    >>> import seaborn as sns
    >>> df = sns.load_data_set('titanic')
    >>> print(get_col_stats(df, 'fare').to_markdown())
    >>> for col in df.columns:
            print(f"column name: {col}")
            print(get_col_stats(df, col).to_markdown())
            print()
    """

    # get frequency counts and % 
    counts = df[col].value_counts(dropna=False)
    pct = df[col].value_counts(dropna=False, normalize=True)

    # convert from series to df for merge
    counts_df = pd.DataFrame(counts).rename(columns={col: 'count'})
    pct_df = pd.DataFrame(pct).rename(columns={col: 'pct'})
    merged = (counts_df.merge(pct_df, left_index=True, right_index=True)
                       .rename_axis(index='value')
                       .reset_index()
             )
    
    if merged.shape[0]>10:
        other_row = pd.DataFrame(merged.iloc[11:].sum()).T
        other_row.value = 'other'
        merged = pd.concat([merged.iloc[:10], other_row]).reset_index(drop=True)

    return merged
```

column name: survived
|    |   value |   count |      pct |
|---:|--------:|--------:|---------:|
|  0 |       0 |     549 | 0.616162 |
|  1 |       1 |     342 | 0.383838 |

column name: pclass
|    |   value |   count |      pct |
|---:|--------:|--------:|---------:|
|  0 |       3 |     491 | 0.551066 |
|  1 |       1 |     216 | 0.242424 |
|  2 |       2 |     184 | 0.20651  |

column name: sex
|    | value   |   count |      pct |
|---:|:--------|--------:|---------:|
|  0 | male    |     577 | 0.647587 |
|  1 | female  |     314 | 0.352413 |

column name: age
|    | value   |   count |       pct |
|---:|:--------|--------:|----------:|
|  0 | nan     |     177 | 0.198653  |
|  1 | 24.0    |      30 | 0.03367   |
|  2 | 22.0    |      27 | 0.030303  |
|  3 | 18.0    |      26 | 0.0291807 |
|  4 | 28.0    |      25 | 0.0280584 |
|  5 | 19.0    |      25 | 0.0280584 |
|  6 | 30.0    |      25 | 0.0280584 |
|  7 | 21.0    |      24 | 0.026936  |
|  8 | 25.0    |      23 | 0.0258137 |
|  9 | 36.0    |      22 | 0.0246914 |
| 10 | other   |     467 | 0.52413   |

column name: sibsp
|    |   value |   count |        pct |
|---:|--------:|--------:|-----------:|
|  0 |       0 |     608 | 0.682379   |
|  1 |       1 |     209 | 0.234568   |
|  2 |       2 |      28 | 0.0314254  |
|  3 |       4 |      18 | 0.020202   |
|  4 |       3 |      16 | 0.0179574  |
|  5 |       8 |       7 | 0.00785634 |
|  6 |       5 |       5 | 0.00561167 |

column name: parch
|    |   value |   count |        pct |
|---:|--------:|--------:|-----------:|
|  0 |       0 |     678 | 0.760943   |
|  1 |       1 |     118 | 0.132435   |
|  2 |       2 |      80 | 0.0897868  |
|  3 |       5 |       5 | 0.00561167 |
|  4 |       3 |       5 | 0.00561167 |
|  5 |       4 |       4 | 0.00448934 |
|  6 |       6 |       1 | 0.00112233 |

column name: fare
|    | value   |   count |       pct |
|---:|:--------|--------:|----------:|
|  0 | 8.05    |      43 | 0.0482604 |
|  1 | 13.0    |      42 | 0.047138  |
|  2 | 7.8958  |      38 | 0.0426487 |
|  3 | 7.75    |      34 | 0.0381594 |
|  4 | 26.0    |      31 | 0.0347924 |
|  5 | 10.5    |      24 | 0.026936  |
|  6 | 7.925   |      18 | 0.020202  |
|  7 | 7.775   |      16 | 0.0179574 |
|  8 | 26.55   |      15 | 0.016835  |
|  9 | 0.0     |      15 | 0.016835  |
| 10 | other   |     600 | 0.673401  |

column name: embarked
|    | value   |   count |        pct |
|---:|:--------|--------:|-----------:|
|  0 | S       |     644 | 0.722783   |
|  1 | C       |     168 | 0.188552   |
|  2 | Q       |      77 | 0.0864198  |
|  3 | nan     |       2 | 0.00224467 |

column name: class
|    | value   |   count |      pct |
|---:|:--------|--------:|---------:|
|  0 | Third   |     491 | 0.551066 |
|  1 | First   |     216 | 0.242424 |
|  2 | Second  |     184 | 0.20651  |

column name: who
|    | value   |   count |       pct |
|---:|:--------|--------:|----------:|
|  0 | man     |     537 | 0.602694  |
|  1 | woman   |     271 | 0.304153  |
|  2 | child   |      83 | 0.0931538 |

column name: adult_male
|    | value   |   count |      pct |
|---:|:--------|--------:|---------:|
|  0 | True    |     537 | 0.602694 |
|  1 | False   |     354 | 0.397306 |

column name: deck
|    | value   |   count |        pct |
|---:|:--------|--------:|-----------:|
|  0 | nan     |     688 | 0.772166   |
|  1 | C       |      59 | 0.0662177  |
|  2 | B       |      47 | 0.0527497  |
|  3 | D       |      33 | 0.037037   |
|  4 | E       |      32 | 0.0359147  |
|  5 | A       |      15 | 0.016835   |
|  6 | F       |      13 | 0.0145903  |
|  7 | G       |       4 | 0.00448934 |

column name: embark_town
|    | value       |   count |        pct |
|---:|:------------|--------:|-----------:|
|  0 | Southampton |     644 | 0.722783   |
|  1 | Cherbourg   |     168 | 0.188552   |
|  2 | Queenstown  |      77 | 0.0864198  |
|  3 | nan         |       2 | 0.00224467 |

column name: alive
|    | value   |   count |      pct |
|---:|:--------|--------:|---------:|
|  0 | no      |     549 | 0.616162 |
|  1 | yes     |     342 | 0.383838 |

column name: alone
|    | value   |   count |      pct |
|---:|:--------|--------:|---------:|
|  0 | True    |     537 | 0.602694 |
|  1 | False   |     354 | 0.397306 |
