# Problem
 Jupyter's shell environment and Python kernel are mismatched. This means running something like `pip install <some_package>` in Jupyter will generally not work [reliably] if you hope to use the package in your current environment.

# Solution
(/workaround)


**via pip**
```python
# Install a pip package in the current Jupyter kernel
import sys
!{sys.executable} -m pip install numpy
```
"That bit of extra boiler-plate makes certain that you are running the pip version associated with the current Python kernel, so that the installed packages can be used in the current notebook."


**via conda**
```python
# Install a conda package in the current Jupyter kernel
import sys
!conda install --yes --prefix {sys.prefix} numpy
```
"That bit of extra boiler-plate makes certain that conda installs the package in the currently-running Jupyter kernel (credit: Min Ragan-Kelley for suggesting this approach)."

# Reference
Great explainer by Jake VanderPlas:
https://jakevdp.github.io/blog/2017/12/05/installing-python-packages-from-jupyter/
