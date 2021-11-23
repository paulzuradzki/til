# Fast bulk copy for PostgreSQL

How to use Postgres copy for fast bulk load
* Remember to create the table before the bulk insert
* AFAIK, python `pyodbc` and `sqlalchemy` do not support postgres' native bulk copy; there is a fast_executemany method that I believe is separate 

psql
```bash
$ copy table_name from /data/file_to_load.csv CSV HEADER QUOTE '"'
```

Python with psycopg2 driver
```python
import psycopg2

filepath = 'data/data_file.csv'
table_name = 'data'
conn = psycopg2.connect(dbname='', user='', password='', host='')

with conn.cursor() as cur:
    with open(filepath) as f:
        cur.copy_expert(f"copy {table_name} from STDIN CSV HEADER QUOTE '\"'", f)
        cur.execute("commit;")
```
