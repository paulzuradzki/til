# Description
Demo of how to self-host simple PyPI server.
- The server is the process that hosts the package index / repository. 
- The client will be the process that either uploads or downloads packages from the index.


# Problem
You need to server your Python packages locally or privately.

# Solution
Host your own simple PyPI Server.

Notes
- Set up HTTPS and authentication for basic security in deployments.
- Consider using `twine` for uploading packages.
- Below is a demo of a basic local dev server.
- Also check out managed services like AWS CodeArtifact and the Microsoft or Google equivalents.

# Server

```
python3 -m venv .venv-server
source .venv-server/bin/activate
pip install -U devpi-server
devpi-init --serverdir ./server
devpi-server --port 4040 --serverdir ./server
devpi use http://localhost:4040
devpi login root --password=''
devpi index -c private-pi

devpi use private-pi
python -m pip download wheel --no-deps & devpi upload wheel-*.whl;
python -m pip download setuptools --no-deps & devpi upload setuptools-*.whl;
```


# Client

Creating packages and uploading to your private package index.
- Say you have a Python package. 
- You first build a distributable file (e.g., tar.gz, zip, or whl).
- Then you need to get it on the package index so yourself or others can retrieve it in the future.

```
python3 -m venv .venv-client
source .venv-client/bin/activate
pip install -U --pre -q devpi-client

# from root of package project
python setup.py sdist
devpi upload /dist/my_package-0.0.1.tar.gz
```

Installing from your private package index.
```
python -m pip install converters --index-url http://localhost:4040/private-pi
```

# References
- https://devpi.net/docs/devpi/devpi/latest/+doc/quickstart-server.html#quickstart-server
