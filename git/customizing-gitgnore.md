# Customizing `.gitignore`

# Problem

I have files locally that I want to exclude from git tracking (ie, to keep IDE source control changes clean) without changing the project `.gitignore`.


# Solution

- If you want to ignore files at the project-level, add your file patterns to `.git/info/exclude` from your project root.

- If you want to ignore files global, do the following:

```bash
# Make global .gitignore
touch ~/.gitignore_global

# Configure git to use it
git config --global core.excludesfile ~/.gitignore

# Verify
git config --get core.excludesfile

# Add patterns ...
```