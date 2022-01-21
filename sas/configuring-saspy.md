# Configuring SASPy
The `saspy` library enables executing SAS programs from Python. The initial configuration is non-trivial. Reference the documentation for various SAS configurations. These steps use the "IOM" connection method for Windows.

# References
* [SASPy docs](https://sassoftware.github.io/saspy)
* [how to set up an _authinfo file for auto password](https://sassoftware.github.io/saspy/configuration.html#the-authinfo-file-authinfo-on-windows)
* [how to encode a SAS password](https://documentation.sas.com/?docsetId=authinfo&docsetTarget=n0xo6z7e98y63dn1fj0g9l2j7oyq.htm&docsetVersion=9.4&locale=en#p1le127swrbmtzn1lwny85q1fyo6)


# Steps
1. [Create and activate a virtual environment](#create-and-activate-a-virtual-environment)
2. [Find and edit the saspy configuration file](#find-and-edit-the-saspy-configuration-file)
3. [Make authinfo file](#make-authinfo-file) (optional)
4. [Test the connection from Python](#test-the-connection-from-python)


### Create and activate a virtual environment

Using venv and pip:
```bash
# creating a virtual environment named venv
$ python -m venv venv

# unix/mac terminal
$ source venv/bin/activate

# windows
$ venv\Scripts\activate

# upgrading pip and installing saspy
# --trusted-host parameter helps avoid https/ssl error if firewall is blocking these repositories
$ python -m pip install --trusted-host pypi.python.org --trusted-host files.pythonhosted.org --trusted-host pypi.org --upgrade pip
$ python -m pip install --trusted-host pypi.python.org --trusted-host files.pythonhosted.org --trusted-host pypi.org saspy pandas
```

Using conda:
```bash
```bash
# temporarily skip ssl verification if running into firewall errors
# install saspy
# reset ssl_verification to 'yes' when you are done (safer)
$ conda config --set ssl_verify no
$ conda install saspy pandas
$ conda config --set ssl_verify no

```

### Find and edit the saspy configuration file
* One way to find this is by using the `sys.path` list in a Python interactive terminal
    * Python stores third-party libraries in a site-packages/ subdirectory with more subdiretories labeled by library (e.g., saspy, pandas)
    * when we `import saspy`, the directories in this list are a few of the places that Python searches for the module
* An alternative on Windows is to go to "This PC" > Properties > Advanced Settings > inspect System Environment Variables
    * You can also search for "environment variables" in Windows search
    * On remote desktop, admin privileges may be required to view using this method

```bash
# enter Python interactive mode in shell and print system paths
$ python
>>> import sys
>>> for p in sys.path: print(p)
C:\Users\pzuradzki\AppData\Local\Continuum\miniconda3\envs\dev\python37.zip
C:\Users\pzuradzki\AppData\Local\Continuum\miniconda3\envs\dev\DLLs
C:\Users\pzuradzki\AppData\Local\Continuum\miniconda3\envs\dev\lib
C:\Users\pzuradzki\AppData\Local\Continuum\miniconda3\envs\dev
C:\Users\pzuradzki\AppData\Local\Continuum\miniconda3\envs\dev\lib\site-packages
C:\Users\pzuradzki\AppData\Local\Continuum\miniconda3\envs\dev\lib\site-packages\locket-0.2.1-py3.7.egg
C:\Users\pzuradzki\AppData\Local\Continuum\miniconda3\envs\dev\lib\site-packages\win32
C:\Users\pzuradzki\AppData\Local\Continuum\miniconda3\envs\dev\lib\site-packages\win32\lib
C:\Users\pzuradzki\AppData\Local\Continuum\miniconda3\envs\dev\lib\site-packages\Pythonwin
```

* In the example output above, the directory we want to explore is the one ending in `site-packages` 
    * `C:\Users\pzuradzki\AppData\Local\Continuum\miniconda3\envs\dev\lib\site-packages`
* Navigate to [...]/site-packages/saspy.
* Make a backup copy of [...]/site-packages/saspy/sascfg.py
* Open sascfg.py for editing
* Replace the dictionary named `default` and add the following
    * The authkey variable is optional. We will use it so we can store our credentials in a separate file so we that don't have to re-enter our username and password on each new SAS connection.

```python
# sascfg.py
SAS_output_options = {'output' : 'html5'}       # not required unless changing any of the default
default = {'iomhost': 'your_sas_server_name',
    'iomport': 8591,
    'class_id': '12345a-12345a-12345a-12345a-12345a',
    'provider': 'sas.iomprovider',
    'encoding': ' latin1',
    'authkey' : 'iomcom_auth'}
``` 

### Make authinfo file
(optional)

First we need to encode our password. Open SAS EG, and run the following command with your password.
```sas
proc pwencode in='yourPassword' method=sas004;  
run;
```

The SAS log will display your encoded password in a format like so: `{SAS004}1234A1234A1234A1234A1234A1234A1234A`. Copy this password into your clipboard.

Create a file named `_authinfo` in your home directory.
* Add a line in the following format. Template: `authkeyName user userName password encodedPassword`
* the authkey name should match the authkey value in sascfg.py
* example:
C:/Users/pzuradzki/_authinfo
```
iomcom_auth user pzuradzki password {SAS004}1234A1234A1234A1234A1234A1234A1234A
```

### Test the connection from Python
If you skipped the _authinfo step, then you should be prompted for a username and password.
```python
import saspy
sas = saspy.SASsession(encoding='latin1')
```
