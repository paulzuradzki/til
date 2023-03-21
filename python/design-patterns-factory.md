# Design Patterns: Factory Method / Virtual Constructor

Notes
* The Factory constructor can return one of multiple objects that implements some common interface
* Using this pattern, you do not instantiate subclasses directly. The Factory does it.
* For example, below, we instantiate DBFactory() and call its `.make_db()` method; but the class that is returned (as `db`) is actually different in 1 of the 3 initializations. 
  * Depending on the `config` that is passed, we either instantiate a `PostgresDB` or `SQLiteDB` class.
  * ex: the with-block using `config_03` is using a Postgres database connection
* From there, you can extend it other subclasses (e.g., database connection types in our example). Other database drivers may have a different API. Using the Factory method, you can standardize the interface and save yourself from messy if-else branching.
* A few extra features in the example:
  * context manager: `__enter__` and `__exit__` takes care of resource setup and cleanup and enables `with` block syntax
  * the abstract base class `DBInterface` defines the common interface that its subclasses must implement; it is not necessary but it signals intent and will be enforced at runtime
    * if you attempt to instantiate a subclass of an ABC without implementing the abstract methods, you will get a runtime error

```python
# client.py

from pprint import pprint

import dotenv

from db import DBFactory

# in-memory SQLite DB
config_01 = {"engine": "sqlite", "database": ":memory:"}
with DBFactory().make_db(config=config_01) as db:
    db.execute("create table foo (col_a int, col_b int);")
    db.execute("insert into foo values (1,2), (3,4);")
    results = db.execute("select * from foo;")
    pprint(results)

# file-based SQLite DB
config_02 = {"engine": "sqlite", "database": "test_db.db"}
with DBFactory().make_db(config=config_02) as db:
    db.execute("drop table if exists foo;")
    db.execute("create table foo (col_a int, col_b int);")
    db.execute("insert into foo values (1,2), (3,4);")
    results = db.execute("select * from foo;")
    pprint(results)

# Postgres DB --> config takes: engine='postgres', host, port, database, user, password
config_03 = dotenv.dotenv_values()
with DBFactory().make_db(config=config_03) as db:
    db.execute("drop table if exists foo; create table foo (col_a int, col_b int);")
    db.execute("insert into foo values (1,2), (3,4);")
    results = db.execute("select * from foo;")
    pprint(results)

# {('col_a', 1): ('col_b', 2), ('col_a', 3): ('col_b', 4)}
# {('col_a', 1): ('col_b', 2), ('col_a', 3): ('col_b', 4)}
# {('col_a', 1): ('col_b', 2), ('col_a', 3): ('col_b', 4)}

```

```python
# db.py

import sqlite3
from abc import ABC, abstractmethod
from typing import Literal

import psycopg2


class DBFactory:
    @classmethod
    def make_db(cls, config):
        engine: Literal["sqlite", "postgres"] = config["engine"]
        if engine == "sqlite":
            return SQLiteDB(config)
        if engine == "postgres":
            return PostgresDB(config)


class DBInterface(ABC):
    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def execute(self):
        pass


class SQLiteDB(DBInterface):
    def __init__(self, config):
        self.database = config["database"]
        self._conn = self.connect()

    def connect(self):
        self._conn = sqlite3.connect(self.database)
        return self._conn

    def execute(self, sql):
        with self._conn:
            cursor = self._conn.cursor()
            cursor.execute(sql)
            self._conn.commit()
            rows = cursor.fetchall()
            if rows:
                cols = [x[0] for x in cursor.description]
            else:
                return []
        return dict([zip(cols, row) for row in rows])

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._conn.close()


class PostgresDB(DBInterface):
    def __init__(self, config):
        self.config = config
        self._conn = self.connect()

    def connect(self):
        return psycopg2.connect(
            host=self.config["host"],
            port=self.config["port"],
            database=self.config["database"],
            user=self.config["user"],
            password=self.config["password"],
        )

    def execute(self, sql):
        with self._conn:
            with self._conn.cursor() as cursor:
                cursor.execute(sql)
                try:
                    rows = cursor.fetchall()
                    cols = [x[0] for x in cursor.description]
                except psycopg2.ProgrammingError:
                    return []
            return dict([zip(cols, row) for row in rows])

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._conn.close()

```
