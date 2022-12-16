References:
* I don't have/remember the link but this example is from one of Matt Harrison's talks (should be on YouTube); author of Effective Pandas

```python
"""pandas tricks
* chaining and pipe for readability
* inspecting intermediate tables with IPython.display in notebook
* assigning intermediate tables to variables with hacky globals() trick

"""
import pandas as pd
import seaborn as sns
from IPython.display import display

def get_power_stats(df):
    return (df.assign(hp_per_lb=df['horsepower']/df['weight'])
            [['name', 'horsepower', 'weight', 'hp_per_lb']]
           )

def get_top_5_power_ratio(df):
    return df.sort_values(by=['hp_per_lb']).iloc[:5, :].reset_index(drop=True)

def format_table(df):
    return (df.assign(name=df.name.str.upper(), 
                      horsepower=df.horsepower.astype('int32'),
                      weight=df.weight.apply(lambda x: '{:,}'.format(x)),
                      hp_per_lb=df.hp_per_lb.apply(lambda x:'{:.4f}'.format(x)),
                     )
           )

def save_df_to_var(df, var_name):
    globals()[var_name] = df
    return df

def inspect_df(df):
    print("(rows, cols):", df.shape)
    return display(df.head(2)) or df
    
df = sns.load_dataset('mpg')

# reads more like English, top-down, left-to-right
processed1 = (df.pipe(get_power_stats)
                .pipe(inspect_df)
                .pipe(save_df_to_var, 'df2')
                .pipe(inspect_df)
                .pipe(get_top_5_power_ratio)
                .pipe(save_df_to_var, 'df3')              
                .pipe(inspect_df)
                .pipe(format_table)
                .pipe(inspect_df)
             )

# functional but requires passing in df as an arg and reasoning right-to-left/from inner to outer
processed2 = get_top_5_power_ratio(get_power_stats(df))
```

(rows, cols): (398, 4)
|    | name                      |   horsepower |   weight |   hp_per_lb |
|---:|:--------------------------|-------------:|---------:|------------:|
|  0 | chevrolet chevelle malibu |          130 |     3504 |   0.0371005 |
|  1 | buick skylark 320         |          165 |     3693 |   0.0446791 |

(rows, cols): (398, 4)
|    | name                      |   horsepower |   weight |   hp_per_lb |
|---:|:--------------------------|-------------:|---------:|------------:|
|  0 | chevrolet chevelle malibu |          130 |     3504 |   0.0371005 |
|  1 | buick skylark 320         |          165 |     3693 |   0.0446791 |

(rows, cols): (5, 4)
|    | name               |   horsepower |   weight |   hp_per_lb |
|---:|:-------------------|-------------:|---------:|------------:|
|  0 | vw dasher (diesel) |           48 |     2335 |   0.0205567 |
|  1 | mercedes-benz 240d |           67 |     3250 |   0.0206154 |

(rows, cols): (5, 4)
|    | name               |   horsepower | weight   |   hp_per_lb |
|---:|:-------------------|-------------:|:---------|------------:|
|  0 | VW DASHER (DIESEL) |           48 | 2,335    |      0.0206 |
|  1 | MERCEDES-BENZ 240D |           67 | 3,250    |      0.0206 |
