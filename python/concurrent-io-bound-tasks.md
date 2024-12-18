# Concurrent Processing Options for IO-bound Tasks

# Problem

You have slow, IO-bound tasks that you want to run concurrently.

```python
import time

def add(a, b):
    time.sleep(3)
    result = a + b
    return result

# Regular I/O bound function
add(2, 3)
```

Slow, non-async loop 🐢

Run time: 9 seconds (3 seconds per loop)
```python
a_b_pairs = [(1, 1), (2, 2), (3, 3)]

results = []
for a, b in a_b_pairs:
    result = add(a, b)
    results.append(result)
    
print(results)
# [2, 4, 6]
```


# Solution

Use any of the options below, which will run in ~3 seconds.

- Multithreading
- asyncio
- Taks queue (Celery)

### Multithreading

```python
from concurrent.futures import ThreadPoolExecutor

a_b_pairs = [(1, 1), (2, 2), (3, 3)]

with ThreadPoolExecutor(max_workers=5) as executor:
    result = executor.map(
        add,
        # iterable containing first argument
        [pair[0] for pair in a_b_pairs],
        # "" for second argument
        [pair[1] for pair in a_b_pairs],
    )

    # Fancy 💅
    # result = executor.map(lambda pair: add(*pair), a_b_pairs)

print(list(result))
# [2, 4, 6]
```

### Using `asyncio`

```python
import asyncio


async def async_add(a, b):
    # Need to use asyncio.sleep to simulate non-blocking behavior b/c time.sleep is blocking
    await asyncio.sleep(3)
    return a + b


async def main():
    a_b_pairs = [(1, 1), (2, 2), (3, 3)]
    tasks = [async_add(pair[0], pair[1]) for pair in a_b_pairs]
    results = await asyncio.gather(*tasks)
    print(results)


# for use alongside Jupyter event loop
# await main()

# for script
asyncio.run(main())
# [2, 4, 6]
```

### Using a task queue

Start Celery service

```bash
# Start message broker (Redis or RabbitMQ)
$ docker run -d -p 6379:6379 redis

# Test
$ redis-cli -h localhost -p 6379 ping
PONG

# Start celery worker
$ celery -A tasks worker --loglevel=INFO
```

Script

```python
"""
Note: Celery workers must be running before executing this module
"""
from celery import Celery

app = Celery("tasks", 
             broker="redis://localhost", 
             backend="redis://localhost"
             )

# Wrap your function in task decorator and call with .delay(*args, **kwargs)
@app.task
def _add(a, b):
    return add(a, b)

# Tasks kicked off. Non-blocking.
result_01 = _add.delay(1,1)
result_02 = _add.delay(2,2)
result_03 = _add.delay(3,3)

# Wait for tasks to finish and get result. result.get() is blocking.
results = [
    result_01.get(),
    result_02.get(),
    result_03.get(),
]

print(results)
# [2, 4, 6]

# Celery logs
# [2024-12-15 23:08:59,637: INFO/MainProcess] Task tasks._add[ec9cadfc-8090-4b70-944d-1f2c5402df94] received
# [2024-12-15 23:08:59,638: INFO/MainProcess] Task tasks._add[60db3760-9af2-49e8-bed9-cdc302e48892] received
# [2024-12-15 23:08:59,639: INFO/MainProcess] Task tasks._add[c8e7de50-028d-449f-aa1c-0c5ff804828a] received
# [2024-12-15 23:09:02,654: INFO/ForkPoolWorker-9] Task tasks._add[c8e7de50-028d-449f-aa1c-0c5ff804828a] succeeded in 3.013587916997494s: 6
# [2024-12-15 23:09:02,653: INFO/ForkPoolWorker-8] Task tasks._add[ec9cadfc-8090-4b70-944d-1f2c5402df94] succeeded in 3.015690625004936s: 2
# [2024-12-15 23:09:02,654: INFO/ForkPoolWorker-1] Task tasks._add[60db3760-9af2-49e8-bed9-cdc302e48892] succeeded in 3.0145508330024313s: 4
```

# Discussion

**IO (input/output) vs CPU-bound tasks**

IO-bound tasks are "waiting" tasks where your CPU sits idle. For example:
- reading from disk (disk I/O)
- reading from a database (network I/O)
- HTTP request (network I/O)

Say you need to need to loop through 1000 URL web requests. That would lead to a lot of wasted time waiting to hear back from remote servers. The idea of concurrent processing here is to have more "workers" start processesses asynchronously (i.e., Celery works for distributed processing, threads for local processing) or to use "cooperative multi-tasking" (asyncio).

For IO-bound tasks, threads are a good first choice.

For CPU-bound tasks (e.g., number crunching), you need more CPU cores for parallelization. For that, we prefer multiprocessing (not demo'ed here).

# Resources

Celery
- Docs: https://docs.celeryq.dev/en/stable/getting-started/introduction.html
- Free tutorials for Django + Celery: https://testdriven.io/guides/django-celery/
- Paid course/guide for Django + Celery: https://testdriven.io/courses/django-celery/

Parallelism in Python
- [Parallel Programming in Python with async/await and threads Course (TalkPython.fm)](https://training.talkpython.fm/courses/explore_async_python/async-in-python-with-threading-and-multiprocessing)
- [Section on Multithreading in Ch17, Automate the Boring Stuff (automatetheboringstuff.com)](https://automatetheboringstuff.com/2e/chapter17/)
- Looking ahead
    - Keep an eye on sub-interpreters (new in Python 3.12)
        - Talk: [Eric Snow: A Per-Interpreter GIL: Concurrency and Parallelism with Subinterpreters (youtube.com)](https://www.youtube.com/watch?v=3ywZjnjeAO4)
    - Consider Rust extensions for performance-critical processing if warranted (complexity, Rust learning curve)
        - [Robin Raymond: Rusty Python - A Case Study (youtube.com)](https://www.youtube.com/watch?v=Y5XQR0wUEyM)