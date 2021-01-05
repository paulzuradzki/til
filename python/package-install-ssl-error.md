# Problem

It appears that corporate proxy/firewall/mitm-box is not allowing traffic to pypi.org and/or files.pythonhosted.org. Using --trusted-host parameter is a workaround. It's worth checking with IT on whether these domains are blocked.

```
python pip install --upgrade pip

-> Error like:
Caused by SSLError(SSLCertVerificationError(1, '[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed

```
References:
* https://python-forum.io/printthread.php?tid=12634
* http://seanlaw.github.io/2015/12/23/fetching-conda-packages-behind-a-firewall/


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
