Logging
```bash
# show filenames associated with each commit
git log -m --name-only --oneline

# show commit tree and branching
  # --abbrev-commit - shorten commit ID
  # --oneline - compressed view
  # --graph - shows branching; also displays commits associated with merge commit
git log --oneline --graph --abbrev-commit

# concise log
git log --oneline

# show differences between the remote main branch and current head
# helps ID which commits are causing "your branch is ahead by N commits" in `git status`
git log origin/main..HEAD --oneline
```
