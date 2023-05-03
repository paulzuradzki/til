# Step into code of third-party packages with debugger

## Problem

By default, the VS Code debugger does not step into the source code of third-party packages.
* e.g., if you use `import pandas as pd` and want to step into `pandas` source code
* or `import my_package` when `my_package` is installed as a package in your PYTHONPATH or site packages
* the VS Code debugger - by default - will only step through `my_package` if the source code is in the the top-level root of your repo, which is not always the case. 
* This is troublesome if you want to debug your own package that is contained in, say, a `./src` directory.
  * E.g., say you've pip-installed your package from source in editable mode (`pip install -e .`). You still want to be able to step through the code using your IDE's debugger.


## Solution
* for VS Code, set `justMyCode` parameter to `false` in your debugger `launch.json` config
* in PyCharm, there is both a `Step Into My Code` and `Step Into` button ([PyCharm docs](https://www.jetbrains.com/help/pycharm/stepping-through-the-program.html))
* less user-friendly but works anywhere: use `pdb`
  * [tutorial via RealPython](https://realpython.com/python-debugging-pdb/)
  * [Python pdb docs](https://docs.python.org/3/library/pdb.html))

```
// ./.vscode/launch.json
{
    // Use IntelliSense to learn about possible attributes.
    // Hover to view descriptions of existing attributes.
    // For more information, visit: https://go.microsoft.com/fwlink/?linkid=830387
    "version": "0.2.0",
    "configurations": [

        {
            "name": "Python: Current File",
            "type": "python",
            "request": "launch",
            "program": "${file}",
            "console": "integratedTerminal",
            "justMyCode": false,
        }
    ]
}
```
