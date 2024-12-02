# Check or Stop Postgres Queries

# Problem

You have some hanging queries or queries that you want to inspect or terminate.


# Solution

Use built-in pg_stat_activity table.

```sql
/* Check active queries */
SELECT pid, state, query, query_start
FROM pg_stat_activity
WHERE state = 'active';


/* Terminate by process ID */
SELECT pg_terminate_backend(pid)
FROM pg_stat_activity
WHERE pid = PID;

/* Terminate all queries on a database */
SELECT pg_terminate_backend(pid)
FROM pg_stat_activity
WHERE datname = 'my_db_name' AND pid <> pg_backend_pid()
;

/* Find long-running queries beyond X interval */
select
    pid,
    usename,
    state,
    query,
    query_start,
    now() - query_start as duration
from
    pg_stat_activity
where
    state = 'active'
    and now() - query_start > interval '10 hour'
  ;
```

FYI that you need superuser or `pg_read_all_stats` role permissions. They can be granted like below.

```sql
GRANT pg_read_all_stats TO your_username;
```

# Docs

- [27.2. The Cumulative Statistics System - Chapter 27. Monitoring Database Activity (postgresql.org)](https://www.postgresql.org/docs/current/monitoring-stats.html)

> *Superusers and roles with privileges of built-in role pg_read_all_stats (see also Section 21.5) can see all the information about all sessions.*
