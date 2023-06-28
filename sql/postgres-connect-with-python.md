# How to connect to a PostgreSQL server from Python

You can connect to a PostgreSQL DB from Python by using `psycopg2` (or now newer `psycopg3`) or `sqlalchemy`.
* SQL Alchemy is an ORM/Object-Relational Mapper which translates many SQL dialects to a common Python object-oriented interface.
  * There are other use case for using an ORM that we won't get into here.
* `psycopg2` is the DB driver that covers most use cases involving "raw" SQL.

# Example

Connecting with both `pyscogp2` and `sqlalchemy`.

```python
import os
from urllib.parse import quote_plus

import dotenv
import psycopg2
import sqlalchemy

# you can load a .env file into a dictionary
       # this is handy if you have name conflicts between variables 
       # and need to switch configurations/credential types like for a prod vs dev DB
       # e.g., env variable 'host' is defined for dev and prod, so you don't want that in your global env
       # (else you may risk inadvertently performing actions on the wrong DB)
db_config = dotenv.dotenv_values('.envs/.env.my_db_config_1')


# you can read env variables from your global environment
       # these variables may be set in your global ~/.bash_profile
       # or you can load them from local .env file with dotenv
       
dotenv.load_dotenv(override=True)

db_config = {'host': os.environ['host'], 
             'database': os.environ['database'], 
             'port': os.environ['port'], 
             'user': os.environ['user'], 
             'password': os.environ['password']
             }

# conn takes: host,user,password,port
conn = psycopg2.connect(**db_config)

# use SQLAlchemy engine for pandas df.to_sql()
# alternatively, url = sqlalchemy.engine.url.URL(<..>)
url = (f"postgresql+psycopg2://{db_config['user']}:{quote_plus(db_config['password'])}"
       f"@{db_config['host']}:{db_config['port']}/{db_config['database']}")
engine = sqlalchemy.create_engine(url)

sql = """\
select *
from information_schema.tables
limit 10;
"""
```

# Links
* https://www.psycopg.org/docs/
* https://docs.sqlalchemy.org/en/20/
* https://github.com/theskumar/python-dotenv
