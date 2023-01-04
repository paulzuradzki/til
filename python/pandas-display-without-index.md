# Problem

I want to display a pandas dataframe without the index.

# Solution

```python
from IPython.display import HTML
import pandas as pd

data = [
 {'sepal_length': 5.1,
  'sepal_width': 3.5,
  'petal_length': 1.4,
  'petal_width': 0.2,
  'species': 'setosa'},
 {'sepal_length': 4.9,
  'sepal_width': 3.0,
  'petal_length': 1.4,
  'petal_width': 0.2,
  'species': 'setosa'},
 ]

df = pd.DataFrame(data)

HTML(
    df
    .to_html(index=False)
)
```

Dataframe without index via HTML:

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>sepal_length</th>
      <th>sepal_width</th>
      <th>petal_length</th>
      <th>petal_width</th>
      <th>species</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>5.1</td>
      <td>3.5</td>
      <td>1.4</td>
      <td>0.2</td>
      <td>setosa</td>
    </tr>
    <tr>
      <td>4.9</td>
      <td>3.0</td>
      <td>1.4</td>
      <td>0.2</td>
      <td>setosa</td>
    </tr>
  </tbody>
</table>
