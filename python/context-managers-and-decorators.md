# Comparing Context Managers and Decorators

# Problem

You want to add behavior to code -- e.g., logging, timing, retries, caching -- without modifying the code. Perhaps the code is code you don't even own like a third-party library, so you need to modify it "from the outside". 

# Solution

You can you decorators and/or context managers.

### Context Manager

Make a class that implements `__enter__` and `__exit__` for your before-after behavior.

```python
import time

class TimeIt:
    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, *args):
        self.end = time.time()
        print('Time taken:', self.end - self.start)
        
with TimeIt():
    for i in range(3):
        time.sleep(.5)
```

### Decorator

```python
def time_it_dec(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print('Time taken:', end - start)
        return result
    return wrapper

@time_it_dec
def do_thing():
    for i in range(3):
        time.sleep(.5)
    return "foo"
        
do_thing()

# Time taken: 1.51161789894104
# 'foo'
```

### Combining context manager and decorator

Using dunder methods

```python
class TimeIt:
    def __init__(self, func=None):
        self.func = func    

    def __call__(self, *args, **kwargs):
        if self.func:
            start = time.time()
            result = self.func(*args, **kwargs)
            end = time.time()
            print('Time taken:', end - start)
            return result
        else:
            return self
        
    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        end = time.time()
        print('Time taken:', end - self.start)
        
        
time_it = TimeIt
```

```python
@TimeIt
def do_thing():
    for i in range(3):
        time.sleep(.5)
    return "foo"

do_thing()
```

```python
@time_it
def do_thing():
    for i in range(3):
        time.sleep(.5)
    return "foo"

do_thing()
```

```python
with TimeIt() as t:
    for i in range(3):
        time.sleep(.5)
```


### Shorthand for context manager only

Using `contextlib.contextmanager`

```python
from contextlib import contextmanager

@contextmanager
def time_it():
    start = time.time()
    yield
    end = time.time()
    print('Time taken:', end - start)

with time_it():
    for i in range(3):
        time.sleep(.5)
```

### Shorthand for context manager and decorator combined

```python
import time
from contextlib import contextmanager, ContextDecorator

class time_it(ContextDecorator):
    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.end = time.time()
        print('Time taken:', self.end - self.start)

@time_it()
def do_thing():
    for i in range(3):
        time.sleep(.5)
    return "foo"


with time_it():
    # Same as do_thing() but without defining function
    for i in range(3):
        time.sleep(.5)

do_thing()
```

# Discussion

On when to use Decorators vs Context Managers: Decorators are good for modifying the behavior of entire functions. For finer-grained control within blocks or parts of a function, you can use a context manager. Context managers do well when you want want temporary, localized behavior.

References
- [decorators and functools.wraps](python/decorators-and-functools-wraps.md)
- Docs: [contextlib.contextmanager](https://docs.python.org/3/library/contextlib.html#contextlib.contextmanager)
