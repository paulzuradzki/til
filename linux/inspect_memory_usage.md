# Problem
* I want to inspect RAM memory and CPU usage of a remote server. I might not have access to the cloud console for pre-made reporting.
* I can use `ps` or `htop` to inspect active processes, but I want to look at historical results and persist them to a log.

# Solution
* Create reports on memory and CPU usage using `vmstat`. 
* Use nohup to run in the background and add results to a log file.

# Example
```bash
$ nohup bash -c "vmstat -S M -t 5 3" > memory_usage.log &
```

Details
* `nohup bash -c "bash_command" &` - `nohup` with `&` executes process in background
  * See [nohup TIL](https://github.com/paulzuradzki/til/blob/master/linux/nohup.md) for more
*  `> log_file.log` - specify log file to create; else, nohup output will be appended to `nohup.out` by default
* `-S M` - specifies memory format in megabytes (1024 bytes to MB)
* `-t` - specifies to add timestamps to output table
* `5 3` - collect statistics every 5 seconds for 3 iterations. The iteration count is optional.

# Example Output

```bash
me@server ~> cat memory_usage.log
procs -----------memory---------- ---swap-- -----io---- -system-- ------cpu----- -----timestamp-----
 r  b   swpd   free   buff  cache   si   so    bi    bo   in   cs us sy id wa st                 UTC
 1  0      0  13833     26    436    0    0    14     2    7    5  1  0 99  0  0 2022-09-08 20:43:34
 0  0      0  13836     26    436    0    0     0    13  613  655  0  0 99  0  0 2022-09-08 20:43:39
 0  0      0  13836     26    436    0    0     0    27 1177 1399  5  0 95  0  0 2022-09-08 20:43:44
```
