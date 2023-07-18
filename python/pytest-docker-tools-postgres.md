# pytest-docker-tools demo with PostgreSQL DB

## Problem

I want to test database operations, but I don't have (or don't want) access to the production database in my tests.

## Solution

* Use [pytest-docker-tools](https://github.com/Jc2k/pytest-docker-tools) to spin up a local Postgres database for testing with Docker.
* Several Python packages exist that provide convenient functions for controlling Docker containers within the scope of pytest tests.


## Example

To clone the full example, see: https://github.com/paulzuradzki/pytest_docker_tools_demo

DB initialization script
* Create a SQL DB table initializer script, which runs automatically when the container starts.
* Alternatively, you run the CREATE TABLE statements directly in your tests.

```sql
/* ./tests/postgres-init.sql */
CREATE TABLE IF NOT EXISTS test (id serial PRIMARY KEY, num integer, data varchar);
```

Test code
* The code is designed to test database operations in isolation by running each test with a clean, temporary PostgreSQL database in a Docker container.
* This approach is useful when you need to test database operations but don't want the tests to affect a persistent database.

```python
# ./tests/test_db.py
import os

import pytest
from psycopg2 import connect
from pytest_docker_tools import container, fetch

# Fetch a PostgreSQL image
postgres_image = fetch(repository="postgres:11")

# Define a container using the image
postgres = container(
    image="{postgres_image.id}",
    environment={"POSTGRES_PASSWORD": "password"},
    ports={"5432/tcp": None},
    volumes={
        os.path.join(os.path.dirname(__file__), "postgres-init.sql"): {
            "bind": "/docker-entrypoint-initdb.d/postgres-init.sql"
        }
    },
)


# Set up a fixture for database connection
@pytest.fixture(scope="function")
def db(postgres):
    """Returns a psycopg2 connection to the test database."""
    docker_port = postgres.ports["5432/tcp"][0]
    conn = connect(
        host="localhost",
        port=docker_port,
        dbname="postgres",
        user="postgres",
        password="password",
    )
    conn.autocommit = True
    yield conn
    conn.close()


# Test case to check simple insert
def test_simple_insert(db):
    cur = db.cursor()
    insert_query_template = "INSERT INTO test (num, data) VALUES (%s, %s)"
    data = [(100, "testdata_foo"), (200, "testdata_bar")]
    cur.executemany(insert_query_template, data)
    cur.execute("SELECT * FROM test;")
    results = cur.fetchall()

    # row 0
    assert results[0][1] == 100
    assert results[0][2] == "testdata_foo"

    # row 1
    assert results[1][1] == 200
    assert results[1][2] == "testdata_bar"

```
