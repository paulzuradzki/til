# Problem

A leading `*` followed by keyword arguments in your function definition will disallow usage of positional arguments if you want to enforce usage of keyword arguments (e.g., more explicit). However, now you have a separate problem if you did not intend for the supplied named arguments to be optional and introduce a bug when the default value is used.

# Solution

Just use positional arguments if they're not optional. The caller will still have ability to use positional or named arguments though.


```python
def concat_no_kwargs(a, b):
    return a + b

def concat_disable_positional_args(*, a=None, b=None):
    return a + b

def concat_optional_kwargs_w_default(a=None, b=None):
    return a + b

x = 'hello, '
y = 'world'

concat_no_kwargs(x, y)          # => 'hello, world'
concat_no_kwargs(a=x, b=y)      # => 'hello, world'
concat_no_kwargs(b=y, a=x)      # => 'hello, world'

concat_disable_positional_args(a=x, b=y) # => 'hello, world'

# => TypeError: concat_disable_positional_args() takes 0 positional arguments but 2 were given
try:
    concat_disable_positional_args(x, y)
except Exception as e:
    pass

# => TypeError: unsupported operand type(s) for +: 'NoneType' and 'NoneType'
try:
    concat_disable_positional_args()
except Exception as e:
    pass

concat_optional_kwargs_w_default(x, y)       # => 'hello, world'
concat_optional_kwargs_w_default(y, x)       # => 'worldhello, '
concat_optional_kwargs_w_default(b=y, a=x)   # => 'hello, world'
```
