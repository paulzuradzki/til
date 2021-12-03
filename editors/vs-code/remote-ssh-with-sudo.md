# Problem
Connecting to a remote server in VS Code with the Remote SSH extension does not allow sudo by default, so you can't open protected files.

# Solution
Modify the SSH config file with the remote command: `RemoteCommand sudo -u dev -i` like below. In VS Code, you can find this under by clicking the Settings gear icon in the Remote Targets section.

```
# .ssh/config/

Host domain.com
  HostName domain.com
  User dev
  RemoteCommand sudo -u dev -i
```
