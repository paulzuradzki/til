# Problem 
File owner naame is not easily obtained from `os.stat(filepath)` on Windows OS. 

# Solution
Use win32 API snippet below.

Adapted from: http://timgolden.me.uk/python/win32_how_do_i/get-the-owner-of-a-file.html

```python
import win32api
import win32con
import win32security

filepath = r'root\dir_01\subdir_01\file_01.txt'

print("I am", win32api.GetUserNameEx (win32con.NameSamCompatible))

sd = win32security.GetFileSecurity(filepath, win32security.OWNER_SECURITY_INFORMATION)
owner_sid = sd.GetSecurityDescriptorOwner ()
name, domain, _type = win32security.LookupAccountSid (None, owner_sid)
print("File owned by %s\\%s" % (domain, name))
```
