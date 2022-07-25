# Problem

I need a way to show diffs between current and previous commit (not unstaged changes) using a relative index where I don't want the commit ID hard-coded.

# Solution

```bash
# brew install ack
# some versions of grep might not support negative lookahead

# show diffs since last commit
# where pattern is subfolder/*.py excluding __init__.py files
git diff --stat --name-only HEAD@{1} HEAD | ack 'subfolder\/(?!__init__).*.py'
```
