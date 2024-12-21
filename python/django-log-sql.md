# Problem

Sometimes you want to see what SQL is being executed by ORM queries.

You can use

```python
from django.db import connection

for q in connection.queries:
    print(q["sql"])
```

... but django.db.connection.queries keeps a log of all queries run in a session.

If you want to debug a single ORM statement, it may generate some X number of queries, 
so you need to slice the list using `len(connection.queries)` before and after your ORM query execution.

# Solution

Use a decorator like below or extract the query counting and slicing logic for your script.

Use with caution! Logs are a source of security risk particularly if they are stored and may reveal sensitive data in the event of a data breach. Parameterized queries help obscure to a certain extent (`%s` placeholders), but this is not a good guarantee. Reserve this logging technique for local debugging.

Usage

```python
from models import MyDjangoORMModel
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

@log_sql(logger=logger)
def make_thing():
    MyDjangoORMModel.objects.create(name="thing")

# fallback to print statements if no logger specified    
@log_sql
def make_thing():
    MyDjangoORMModel.objects.create(name="thing")
```

Decorator

```python
from functools import wraps

import sqlparse
from django.db import connection


def log_sql(func=None, *, logger=None):
    """Utility decorator to display formatted SQL that is executed from an ORM query.
    
    For logger or print debugging. 
    
    `django.db.connection.queries` shows all queries run in a session.
    This decorator helps slice the query collection to only the queries
    that are run in the context of the decorated function.

    We wrap the decorator `log_sql_decorator` in a function `log_sql`
    in order to support a decorator that can be called with keyword args.

    Example usage
    -------------
    >>> from models import MyDjangoORMModel
    >>> import logging
    >>> logger = logging.getLogger(__name__)
    >>> logger.setLevel(logging.DEBUG)
    >>> @log_sql(logger=logger)
        def make_thing():
            MyDjangoORMModel.objects.create(name="thing")

    # fallback to print statements if no logger specified    
    >>> @log_sql
        def make_thing():
            MyDjangoORMModel.objects.create(name="thing")
    """
    def log_sql_decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # BEFORE ORM QUERY
            n_queries_before = len(connection.queries)

            # CALL / EXECUTE ORM QUERY
            func(*args, **kwargs)

            # AFTER
            n_queries_after = len(connection.queries)
            queries_ran = [q['sql'] for q in connection.queries[n_queries_before:]]
            n_queries_ran = len(queries_ran)
            query_counts = {
                "n_queries_before": n_queries_before,
                "n_queries_after": n_queries_after,
                "n_queries_ran": n_queries_ran,
            }

            formatted_queries = [sqlparse.format(sql, reindent=True) for sql in queries_ran]
            formatted_sql = "\n".join(formatted_queries)

            if logger:
                logger.debug("\n"+formatted_sql)
                logger.debug(query_counts)
            else:
                print("\n"+formatted_sql)
                print(query_counts)

        return wrapper

    if func:
        return log_sql_decorator(func)
    return log_sql_decorator
```