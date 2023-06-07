# Example connection string for MS SQL Server

```python
import os
import pyodbc

# SERVER_NAME is an environment variable that is assumed to be defined
conn = pyodbc.connect('DRIVER={SQL Server};SERVER=os.environ['SERVER_NAME'];Trusted_Connection=yes')
```
