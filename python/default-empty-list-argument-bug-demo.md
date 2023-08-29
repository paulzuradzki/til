# Problem

Using an empty list as a default argument in a function can lead to subtle bugs due to pass-by-reference behavior.

*Example*

Here you might expect the second function call to return `['foo']` but it hangs on to state from prior calls.

```python
def add_item(new_item: str, my_list:list[str]=[]):
    my_list.append(new_item)
    return my_list
    
print(add_item('foo'))      # => ['foo']

# Retains 'bar' item from prior call
print(add_item('bar'))      # => ['foo', 'bar']
```

# Solution

Default to `None` and initialize the list inside the function if it's empty.

```python
from typing import Optional

def add_item_v2(new_item: str, my_list: Optional[list[str]]=None):
    if not my_list:
        my_list = []        
    my_list.append(new_item)
    return my_list
    
print(add_item_v2('foo'))       # ['foo']
print(add_item_v2('bar'))       # => ['bar']
```
