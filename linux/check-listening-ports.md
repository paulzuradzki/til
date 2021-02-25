
Command
```bash
$ sudo netstat -tunlp

# filter to port 22
$ sudo netstat -tnlp | grep :22

# ss is the "new" netstat
$ sudo ss -tunlp
```

The options used in this command have the following meaning:
* -t - Show TCP ports.
* -u - Show UDP ports.
* -n - Show numerical addresses instead of resolving hosts.
* -l - Show only listening ports.
* -p - Show the PID and name of the listener’s process. This information is shown only if you run the command as root or sudo user.

source: https://linuxize.com/post/check-listening-ports-linux/
