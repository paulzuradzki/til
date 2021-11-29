```python

import pyodbc
import os

# SERVER_NAME is an environment variable that is assumed to be defined
conn = pyodbc.connect('DRIVER={SQL Server};SERVER=os.environ['SERVER_NAME'];Trusted_Connection=yes')
```
