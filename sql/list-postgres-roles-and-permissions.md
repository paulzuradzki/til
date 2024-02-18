# List postgres roles and permissions

# Problem

You want to know who are the available users and permissions in a PostgreSQL database.

# Solution

```sql
select
    rolname,
    rolsuper,
    rolcreaterole,
    rolcreatedb,
    rolcanlogin
from
    pg_roles;
```
