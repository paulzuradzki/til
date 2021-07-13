# Problem
I want a way to display several dataframes side-by-side (e.g., to demo intermediate steps) in Jupyter without fussing with prints or using the repr in separate cells.

# Solution

```python
import pandas as pd
import numpy as np

class display(object):
    """Display HTML representation of multiple objects"""
    template = """<div style="float: left; padding: 10px;">
    <p style='font-family:"Courier New", Courier, monospace'>{0}</p>{1}
    </div>"""
    def __init__(self, *args):
        self.args = args
        
    def _repr_html_(self):
        return '\n'.join(self.template.format(a, eval(a)._repr_html_())
                         for a in self.args)
    
    def __repr__(self):
        return '\n\n'.join(a + '\n' + repr(eval(a))
                           for a in self.args)

df_a = pd.DataFrame({'col_a': [1, 2, 3], 'col_b': [4, 5, 6]})
df_b = pd.DataFrame({'foo': [np.random.randint(1,10) for n in range(5)]})
df_c = pd.DataFrame({'foo': ['yow'], 'bar': ['grok']})

display('df_a', 'df_b', 'df_c')
```


|    |   col_a |   col_b |
|---:|--------:|--------:|
|  0 |       1 |       4 |
|  1 |       2 |       5 |
|  2 |       3 |       6 |

|    |   foo |
|---:|------:|
|  0 |     8 |
|  1 |     4 |
|  2 |     2 |
|  3 |     1 |
|  4 |     6 |

|    | foo   | bar   |
|---:|:------|:------|
|  0 | yow   | grok  |

Source: Jake Vanderplas via https://jakevdp.github.io/PythonDataScienceHandbook/03.08-aggregation-and-grouping.html
