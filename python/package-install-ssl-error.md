# Problem
Cannot install Python packages possibly due to firewall or inability to verify SSL for Python package repository site.

Your corporate proxy/firewall/mitm-box may not allow traffic to pypi.org and/or files.pythonhosted.org. Using --trusted-host parameter is a workaround. It may be worth checking with IT on whether these domains are blocked.

```shell
$ python -m pip install --upgrade pip
Caused by SSLError(SSLCertVerificationError(1, '[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed
```

Or
```bash
$ python -m pip install --upgrade pip
Retrying (Retry(total=4, connect=None, read=None, redirect=None, status=None)) after connection broken by 'NewConnectionError('<urllib3.connection.VerifiedHTTPSConnection object at 0x7f30a7aa4590>: Failed to establish a new connection: [Errno 101] Network is unreachable')': /simple/pip/
Retrying (Retry(total=3, connect=None, read=None, redirect=None, status=None)) after connection broken by 'NewConnectionError('<urllib3.connection.VerifiedHTTPSConnection object at 0x7f30a7aa4d10>: Failed to establish a new connection: [Errno 101] Network is unreachable')': /simple/pip/
Retrying (Retry(total=2, connect=None, read=None, redirect=None, status=None)) after connection broken by 'NewConnectionError('<urllib3.connection.VerifiedHTTPSConnection object at 0x7f30a7aa4dd0>: Failed to establish a new connection: [Errno 101] Network is unreachable')': /simple/pip/
Retrying (Retry(total=1, connect=None, read=None, redirect=None, status=None)) after connection broken by 'NewConnectionError('<urllib3.connection.VerifiedHTTPSConnection object at 0x7f30a7aa4d50>: Failed to establish a new connection: [Errno 101] Network is unreachable')': /simple/pip/
Retrying (Retry(total=0, connect=None, read=None, redirect=None, status=None)) after connection broken by 'NewConnectionError('<urllib3.connection.VerifiedHTTPSConnection object at 0x7f30a7abd0d0>: Failed to establish a new connection: [Errno 101] Network is unreachable')': /simple/pip/
```

# Solution
```shell
pip install --trusted-host pypi.python.org --trusted-host files.pythonhosted.org --trusted-host pypi.org <package name ex: pandas>

# if you need to pin the version
pip install --trusted-host pypi.python.org --trusted-host pypi.org --trusted-host files.pythonhosted.org <package name>[=0.1.2]
```

For conda
```shell
# warning: not safe
conda config --set ssl_verify no
```

If the server you are installing on is behind a proxy server (your server does not publicly face the internet), then you may need to set an environment variable like so.
```shell
HTTPS_PROXY=http://subdomain.YourDomain.com:3128
export https_proxy="$HTTPS_PROXY"
```

References:
* https://python-forum.io/printthread.php?tid=12634
* http://seanlaw.github.io/2015/12/23/fetching-conda-packages-behind-a-firewall/
* https://jupyterlab.readthedocs.io/en/latest/getting_started/installation.html
