# Problem

* You create a new project and virtual environment in VS Code and want to use VS Code Jupyter Notebook support.
* Desplite having your Python interpreter selected for VS Code, you are unable to run Python from a Jupyter Notebook using your project's virtual env.

# Solution
* You need to run the `ipykernel install` commmand and link the name to your virtual environment. 
* Then the Jupyter kernel should appear as an option in the Change Kernel menu.

```bash
python -m venv venv
source venv/bin/activate
(venv) python -m pip install --upgrade pip
(venv) python -m pip install jupyter ipykernel
(venv) python -m ipykernel install --user --name=venv
```
