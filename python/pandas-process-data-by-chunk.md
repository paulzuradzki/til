
```python
import pandas as pd

# filter data set on import
iter_csv = pd.read_csv('file.csv', iterator=True, chunksize=1000)
df = pd.concat([chunk[chunk['field'] > constant] for chunk in iter_csv])
```

```python
with pd.read_csv("tmp.sv", sep="|", chunksize=4) as reader:
    for chunk in reader:
        print(chunk)
```
See:

https://pandas.pydata.org/pandas-docs/stable/user_guide/io.html#iterating-through-files-chunk-by-chunk
