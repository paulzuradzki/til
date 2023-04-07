# Problem

I want a template file for common Python git ignore-or-include directives.

# Solution

```bash
# .gitignore

# compiled Python
__pycache__/

# MacOS Desktop Services
.DS_Store

# virtual envs
venv/
.venv/

# ignore environment files
.env/
*.env*

# except for .env.example
!*.env.example

# Jupyter IPython notebook
*.ipynb

# temporary Jupyter IPython notebook files
.ipynb_checkpoints/
```
