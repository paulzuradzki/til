```python
def undecorated_greeter(name: str='World'):
    """Prints a greeting"""
    print(f'Hello, {name}!')

def trace(func):
    """Logs the calling of a function"""
    def f(*args, **kwargs):
        print(f'Calling: {func.__name__}')
        return func(*args, **kwargs)
    return f

@trace
def greeter2(name:str ='World'):
    """Prints a greeting"""
    print(f'Hello, {name}!')

# without syntactic convenience of @ symbol
greeter = trace(undecorated_greeter)

greeter('Mando')
print()
greeter2('Mando')
```

```
Calling: undecorated_greeter
Hello, Mando!

Calling: greeter2
Hello, Mando!
```

```python
print('undecorated_greeter doc:', undecorated_greeter.__doc__)
print('undecorated_greeter type annotations:', undecorated_greeter.__annotations__)
print()


print('We lose metadata of the original function after decorating...')
print('greeter doc:', greeter2.__doc__)
print('greeter type annotations:', greeter2.__annotations__)
```

```
undecorated_greeter doc: Prints a greeting
undecorated_greeter type annotations: {'name': <class 'str'>}

We lose metadata of the original function after decorating...
greeter doc: None
greeter type annotations: {}
```

Use functools @wraps to preserve metadata

```python
from functools import wraps

def greeter(name: str='World'):
    """Prints a greeting"""
    print(f'Hello, {name}!')

def trace(func):
    """Logs the calling of a function"""
    @wraps
    def f(*args, **kwargs):
        print(f'Calling: {func.__name__}')
        print(f'Calling: {func.__doc__}')        
        return func(*args, **kwargs)
    return f

print('greeter doc:', greeter.__doc__)
print('greeter type annotations:', greeter.__annotations__)
```

```
greeter doc: Prints a greeting
greeter type annotations: {'name': <class 'str'>}
```
