# SQL Formatting in Python

# Problem

I have unformatted SQL from my own query or an ORM query like below.


```python
sql = "select a, b, c from table where a = 1 and b = 2"

# django query_set.query gives sql on one line
sql = str(query_set.query)
```
# Solution


Try [sqlparse (github.com)](https://github.com/andialbrecht/sqlparse) formatter:

```python
import sqlparse

sql = "select a, b, c from table where a = 1 and b = 2"
parsed = sqlparse.format(sql, reindent=True, keyword_case="upper")
print(parsed)
# SELECT a,
#        b,
#        c
# FROM TABLE
# WHERE a = 1
#   AND b = 2
```

#python
#sql