# Problem
Default pandas to_sql method and SQL loading from Python implement separate insert statements for each recordm, which is very slow.

Assumption: client user does not have BULK INSERT permissions on the server.

# Solution
Try SQLAlchemy fast_executemany mode for writing to SQL Server.
This treats the operation as a single insert.
Postgres COPY or MSSQL BULK INSERT is even better if available.

```
import pandas as pd
import numpy as np
from sqlalchemy import create_engine

# random ints from 0 to 5; array of 5
df = pd.DataFrame({'a': np.random.randint(0,5,5), 
                   'b': np.random.randint(0,5,5)})

print(df.to_markdown())

db_config = {'server': None, 'database': None}
db_conn_str = f"mssql+pyodbc:///?odbc_connect=DRIVER=ODBC Driver 17 for SQL Server;SERVER={server};DATABASE={database};Trusted_Connection=yes"
engine = create_engine(db_conn_str, fast_executemany=True)
df.to_sql(name='table_name', schema='dev',
                    con=engine, if_exists='replace', 
                    index=False)
```

|    |   a |   b |
|---:|----:|----:|
|  0 |   2 |   2 |
|  1 |   4 |   0 |
|  2 |   3 |   3 |
|  3 |   3 |   1 |
|  4 |   0 |   2 |
