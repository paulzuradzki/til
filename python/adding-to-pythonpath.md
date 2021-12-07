For Unix systems, this is how to append a directory to the PYTHONPATH environment variable by appending to itself.

This is can also go in the `.bashrc` or `.bash_profile`. `.bashrc` is started on every new login shell (ideally kept minimalist). `.bash_profile` is for any new shell.

```bash
export PYTHONPATH=$PYTHONPATH:/<path_to_modules>
```

<br><br>
Example use case:

Re-configure Superset's metadatabase to use a non-default DB (ex: PostgreSQL instead of SQLite) by modifying local superset_config.py and adding it to the Python path.
https://superset.apache.org/docs/installation/configuring-superset

`export PYTHONPATH=$PYTHONPATH:/<path_of_dir_where_superset_config_is_located>`
