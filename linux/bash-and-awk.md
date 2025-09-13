Bash and `awk` tricks

```bash
# Add files that were Modified or Deleted (ignore untracked/??)
$ git status --porcelain \
| awk '$1 != "??" {print $2}' \
| xargs git add

# Restore files that match some pattern
$ git status --porcelain \      # pretty-print git status for parsing
  | awk '{print $2}' \          # extract file paths; second column ($2) is filepath
  | grep -E '^pattern/' \        # filter for "pattern/" files only; -E extended grep / egrep
  | xargs git restore           # restore the files; passed as multiple file args via xargs
```
