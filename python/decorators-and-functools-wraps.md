# Decorators and `functools.wraps`

## Question: "what is the use of functools.wraps?"

<br>

## Short answer

The `functools.wraps` updates a decorated function with its original function's metadata such as `func.__name__` (function name) and `func.__doc__` (docstring). This is useful because, unfortunately by default, when you decorate a function, you lose this metadata as it is replaced by the wrapper function.

<br>

___

<br>

## Example

<br>

### Without `functools.wraps`

```python
def greeter(name="World"):
    """Prints a greeting to a supplied name."""
    print(f"Hello, {name}!")

def logged(func, *args, **kwargs):
    def add_loggging(*args, **kwargs):
        print(f"Callling {func.__name__}")
        func(*args, **kwargs)
        print(f"Finished {func.__name__}")
        print()
    return add_loggging

greeter = logged(greeter)

greeter()                       # prints: Hello, World!
greeter(name="Paul")            # prints: Hello, Paul!

#####################
# Here is our problem
#####################
# greeter() lost it's name and docstring to add_logging
print(greeter.__name__)         # prints: add_loggging
print(greeter.__doc__)          # prints: None
```


### With `functools.wraps`
* Note that `greeter.__name__` and `greeter.__doc__` preserve their values from the original `greeter` function even after we decorate `greeter` with `logged`.
* The only difference inside the `logged` function is that we added `@wraps(func)` to the decorator's (`logged`) internal wrapper function.

```python
from functools import wraps

def logged(func, *args, **kwargs):
    @wraps(func)
    def add_logging(*args, **kwargs):
        print(f"Callling {func.__name__}")
        func(*args, **kwargs)
        print(f"Finished {func.__name__}")
    return add_logging

def greeter(name="World"):
    """Prints a greeting to a supplied name."""
    print(f"Hello, {name}!")

greeter = logged(greeter)
    
greeter()                   # prints: Hello, World!
print()
greeter(name="Paul")        # prints: Hello, Paul!

# using functools.wraps decorator, we transfer metadata of the original function
# (like name and docstring) to the decorated function
print()
print(greeter.__name__)     # prints: greeter
print(greeter.__doc__)      # prints: Prints a greeting to a supplied name.
```
<br>

___

<br>

## References

See documentation for `functools.wraps` and `functools.update_wrapper`
* https://docs.python.org/3/library/functools.html#functools.wraps
* https://docs.python.org/3/library/functools.html#functools.update_wrapper

<br>

___

<br>

## Appendix - Decorators

### First, what is a decorator?
* A decorator is a function that modifies the behavior of another function without changing it's definition.
* This is handy when you need to inject functionality but don't want to touch the internals of a function for whatever reason. This may be for code re-use (you don't want to re-write the new functionality in each function), separation of concerns, or perhaps you don't own the definition of the function that you want to modify (e.g., third-party library).
* Some practical use cases for decorators are:
  * Logging
  * Authentication and Authorization
  * Caching and Memoization
  * Timing and Profiling
  * Input Validation
  * Retry Mechanism
  * API Rate Limiting
  * Context Management
* Web frameworks like `Flask`, `Django`, and `FastAPI` have interesting uses for decorators to implement features like routing URLs to views and defining HTTP methods for a URL route.

### More detailed explanation of our decorated `greeter` function:
* We have a function `greeter` that takes an optional keyword argument `name`. The injected behavior that we want is to print the name of the function before and after it is called.
* We will create a decorator function `logged` that takes a function as input and returns a function with this modified behavior. 
    * Sidenote: a function that takes a function as a parameter or has a function as its return value is more generally known as a "higher order function". Programming languages that support or encourage this pattern are also said to have "functions as first-class citizens".


The statement
```python
greeter = logged(greeter)
```

has the same effect as

```python
@logged
def greeter(name="World"):
    """Prints a greeting to a supplied name."""
    print(f"Hello, {name}!")
```

The `@` symbol gives us syntax sugar (Python shorthand) for applying a decorator to a function.
