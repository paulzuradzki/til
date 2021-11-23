# How to connect to a PostgreSQL server from Python

Snippet
```python
# use psycopg2 connections for query execution
conn = psycopg2.connect(dbname=self.DB_NAME, user=self.DB_USER, password=self.DB_PASS, host=self.DB_HOST)

# use SQLAlchemy engine for pandas df.to_sql()
engine = create_engine(f'postgresql+psycopg2://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}/{self.DB_NAME}')
```

Example
```python
import os
from sqlalchemy import create_engine
import psycopg2
import pyodbc

class DBLoader:
    
    def __init__(self, db_user=None, db_pass=None, db_host=None, db_name=None):
        self.DB_USER = db_user
        self.DB_PASS = db_pass
        self.DB_HOST = db_host
        self.DB_NAME = db_name
        
        # use psycopg2 connections for query execution
        self.conn = psycopg2.connect(dbname=self.DB_NAME, user=self.DB_USER, password=self.DB_PASS, host=self.DB_HOST)

        # use SQLAlchemy engine for pandas df.to_sql()
        self.engine = create_engine(f'postgresql+psycopg2://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}/{self.DB_NAME}')
        
    def __repr__(self):
        return f"DBLoader(DB_USER={self.DB_USER}, DB_PASS=*, DB_HOST={self.DB_HOST}, DB_NAME={self.DB_NAME})"


# now we can use dbl.conn or dbl.engine
    # Linux/Mac: export secrets to environment variables in in .bashrc or .zprofile
    # export DB_USER="" ... etc
dbl = DBLoader(db_user=os.environ['DB_USER'], 
               db_pass=os.environ['DB_PASS'], 
               db_host='SERVER_NAME_OR_IP', 
               db_name='DB_NAME')

```
