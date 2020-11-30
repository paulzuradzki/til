# Problem

It appears that corporate proxy/firewall/mitm-box is not allowing traffic to pypi.org and/or files.pythonhosted.org. Using --trusted-host parameter is a workaround. It's worth checking with IT on whether these domains are blocked.

```
python -m pip install --trusted-host pypi.python.org --trusted-host files.pythonhosted.org --trusted-host pypi.org --upgrade pip

-> Error like:
Caused by SSLError(SSLCertVerificationError(1, '[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed

```
Source:
https://python-forum.io/printthread.php?tid=12634

# Solution
```shell
pip install --trusted-host pypi.python.org --trusted-host files.pythonhosted.org --trusted-host pypi.org <package name ex: pandas>
```
