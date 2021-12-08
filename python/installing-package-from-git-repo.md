# Installing a Python Package from a Git Repository

To pip install from a private repo, use the `git+` prefix. Use the URL suffix to specify a particular branch.
```bash
$ python -m pip install git+https://github.com/user/your_package.git

# specify a branch
$ pip install git+https://github.com/user/your_package.git@dev-branch
$ pip install git+https://github.com/user/your_package.git@issue/34/foo-0.6
```

To publish a package publically to PyPI, see this tutorial.
* https://realpython.com/pypi-publish-python-package
* This will make the package installable using a public alias: `python -m pip install your_package`

References on how to structure a package and distribute it:
* Packaging
  * https://dabeaz-course.github.io/practical-python/Notes/09_Packages/01_Packages.html
  * note use of `__init__.py` to stitch modules together into an easier interface for users  
* Distribution
  * https://dabeaz-course.github.io/practical-python/Notes/09_Packages/03_Distribution.html
  * You can pip install from the resulting zip file locally
  * or post to remote repository
  * or publish to PyPI
