# psycopg2 connection and cursor commit behavior for PostgreSQL

### Problem
* I forget when I have to explicitly `commit` transactions for SQL actions that must persist using `psycopg2` (Python driver for postgres).
* You can use both `psycopg2.connection` and `psycopg2.cursor` classes as context managers, so it's easy to forget which one takes care of commits vs. closing a cursor or connection.

### Solution
* Here is a script demonstrating the usage of the `psycopg2.connection` class with and without a context manager (with-block)
  * We still use a context manager on the `psycopg2.cursor` in both `CREATE TABLE` examples
* Only the psycopg2.connection class automatically commits when using a with-block (context manager).
* To further confuse things, the connection remains open outside of the context manager. 
  * The user should be aware that the setup/teardown stops at committing the transaction when using `with conn:...`
* psycopg2 also supports an `autocommit` mode (`psycopg2.connection(autocommit=True)`

```python
import os
from pprint import pprint

import dotenv
import psycopg2

dotenv.load_dotenv(override=True)

conn = psycopg2.connect(
	host=os.environ['host'],
	database=os.environ['database'],
	port=os.environ['port'],
	user=os.environ['user'],
	password=os.environ['password'],
)

# the table 'foo' will get created without calling conn.commit()
    # this behavior is enabled when we use the connection class as a context manager
    # the connection still remains open outside the WITH block though
with conn:
    with conn.cursor() as csr:
        csr.execute("drop table if exists foo; create table foo (col_a int, col_b int);")

# the table 'bar' will only get created if we explicitly commit
with conn.cursor() as csr:
    csr.execute("drop table if exists bar; create table bar (col_a int, col_b int);")
conn.commit()

# if we had not called conn.commit(), then the table 'bar' would only be visible in our Python connection (not to other users or connections)
with conn.cursor() as csr:
    csr.execute("select table_schema, table_name from information_schema.tables where table_schema = 'public';")
    columns = [col.name for col in csr.description]    
    data = [dict(zip(columns, row)) for row in csr.fetchall()]
    
pprint(data)
# [{'table_name': 'foo', 'table_schema': 'public'},
#  {'table_name': 'bar', 'table_schema': 'public'}]
```

### References
* https://www.psycopg.org/docs/connection.html#connection
* https://www.psycopg.org/docs/connection.html#connection.commit
