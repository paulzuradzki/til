Here is an example of how to run steps that must wait on other steps/events before proceeding.

Step 2 and Step 3 can both start once Step 1 is complete. Step 3 will complete first, because Step 2 takes longer (sleeps for 3 seconds).

```python
import threading
import time

def step1(evt):
    print('Step 1')
    time.sleep(1)
    evt.set()

def step2(evt):
    evt.wait()
    time.sleep(3)
    print('Step 2')

def step3(evt):
    evt.wait()
    print('Step 3')

_event_step1_complete = threading.Event()

threading.Thread(target=step1, args=[_event_step1_complete]).start()
threading.Thread(target=step2, args=[_event_step1_complete]).start()
threading.Thread(target=step3, args=[_event_step1_complete]).start()
```

Output
```
Step 1
Step 3
Step 2
```
