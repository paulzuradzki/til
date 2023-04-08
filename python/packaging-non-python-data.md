# Problem
* In your Python package, you have package data in non-Python files (`data.json`, `query.sql`) that you want to ship with your package
* Relative imports will not work, because your package should not assume it is in any particular directory with access to the package source code

# Solution
* Use `MANIFEST.in` file [directives](https://packaging.python.org/en/latest/guides/using-manifest-in/#manifest-in-commands) to specify non-Python files to include in the source distribution
* Use `setup.cfg` file `include_package_data=True` directive to specify that non-Python files in the source distribution should also be included in the binary distribution
* Use the `pkg_resources` module that comes with `setuptools`
  * Instead of passing a file path to something like the `open()` function, you pass: `pkg_resources.resource_filename('package_name', 'relative_path_to_file.txt')`
  * You can install `setuptools` manually with `pip`, but it should be a build pre-requisite in `pyproject.toml`.

```
# https://setuptools.pypa.io/en/latest/pkg_resources.html
Use of pkg_resources is deprecated in favor of importlib.resources, importlib.metadata and their backports (importlib_resources, importlib_metadata). Users should refrain from new usage of pkg_resources and should work to port to importlib-based solutions.
```

Sample `pyproject.toml`
```bash
# pyproject.toml
[build-system] 
requires = ["setuptools", "wheel"] 
build-backend = "setuptools.build_meta" 
```

Sample `setup.cfg`. 
* For package data, you want `include_package_data = True`. 
* This tells `setuptools` to include non-Python files in the binary distribution that are contained in the source distribution.

```bash
# setup.cfg
[metadata]
name = my_package_name
version = 0.0.1
url = https://github.com/user/my_package_name
description = A package.
long_description = file: README.md
long_description_content_type = text/markdown

[options]
package_dir =
    = src
packages = find:
include_package_data = True
python_requires = >=3.6
install_requires =
    pandas
    ipython
    seaborn
    sqlalchemy
    psycopg2

[options.packages.find]
where = src
exclude =
    test*
```


Example usage of non-Python data within your package:
```python
import pkg_resources

with open(pkg_resources.resource_filename('package_name', 'sql/my_query.sql')
          ) as f:
    sql = f.read()

# instead of
# with open('sql/my_query.sql') as f:
#   sql = f.read()

```
