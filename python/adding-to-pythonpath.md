For Unix systems, this is how to append a directory to the PYTHONPATH environment variable by appending to itself.

This is can also go in the `.bashrc` or `.bash_profile`. `.bashrc` is started on every new login shell (ideally kept minimalist). `.bash_profile` is for any new shell.

```bash
export PYTHONPATH=$PYTHONPATH:/<path_to_modules>
```
