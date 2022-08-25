# Problem

You want your process to continue running on a remote SSH connection even if your local machine disconnects or goes to sleep.

# Solution
* Use nohup/"no signal hangup" to run commands in the background
* Appending `&` will run process in background
* `nohup` redirects output to `nohup.out` by default

### Usage

Script
```python
# sleep.py
import time

with open('output.txt', 'w') as f:
    for n in reversed(range(1,11)):
        time.sleep(1)
        print(n)
```

Terminal
```bash
$ nohup --help

# run a process in background
$ nohup [command] &
$ nohup python sleep.py &

# bring command to foreground
$ fg

# run multiple processes in background
  # `-c` executes bash from string
$ nohup bash -c '[command1] && [command2]' &
$ nohup bash -c 'python sleep.py && python sleep.py' &

# run in background and redirect output
$ nohup python sleep.py > out.txt & 
```

References
* https://phoenixnap.com/kb/linux-nohup
  * "Although nohup may appear similar to daemons, there is a significant difference. Daemons are reserved for processes that continuously run in the background, while nohup is used for processes that take a long time but don't continue running once done."
