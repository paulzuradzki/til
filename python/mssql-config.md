# Problem
I want to use SQLAlchemy's fast_executemany=True setting for faster writes to MSSQL. The SQL connection string is also finnicky depending on the database driver being used.

# Solution

Identify the database driver and fill the conn_str (connection string) parameters like below. Avoid the `SQL Server` driver, which is older and causes a memory error when using `fast_executemany=True`. 



```python
import numpy as np
import pandas as pd
import pyodbc
from sqlalchemy import create_engine

data = np.ones((5,3), 'int')
headers = ['col_a', 'col_b', 'col_c']
df = pd.DataFrame(data, columns=headers)

DATABASE = 'DB_NAME'
DRIVER = 'SQL Server Native Client 11.0'.replace(' ', '+')
SERVER = 'SERVER_NAME'

conn_str = f"mssql+pyodbc://{SERVER}/{DATABASE}?&driver={DRIVER}&Trusted_Connection=yes"
engine = create_engine(conn_str, fast_executemany=True)

df.to_sql(name='test_load', 
          schema='dev', 
          con=engine, 
          if_exists='replace', 
          index=False)

print('SQL Drivers:')
for driver in pyodbc.drivers():
    if 'SQL' in driver:
        print('\t', driver)
```

Output
```
SQL Drivers:
	 SQL Server
	 SQL Server Native Client 11.0
	 ODBC Driver 11 for SQL Server
```

Resulting table
```
|    |   col_a |   col_b |   col_c |
|---:|--------:|--------:|--------:|
|  0 |       1 |       1 |       1 |
|  1 |       1 |       1 |       1 |
|  2 |       1 |       1 |       1 |
|  3 |       1 |       1 |       1 |
|  4 |       1 |       1 |       1 |
```
