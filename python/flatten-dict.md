# Example 1

```python
from typing import Dict, List, Union

def flatten(data: List[Union[Dict, List]]) -> List[Dict]:
    """Flatten nested lists of dictionary to single list of dictionaries.
    
    Dictionaries in sub-lists/JSON arrays will be moved to the outer level.
    
    Usage
    -----
    >>> data = [{1: 'one', 2: 'two'}, 
                [{3: 'three', 4: 'four'}, {5: 'five', 6: 'six'}], 
               ]       
    >>> [item for item in flatten(data)]    # -> [{1: 'one', 2: 'two'}, {3: 'three', 4: 'four'}, {5: 'five', 6: 'six'}]
    """
    
    for item in data:
        if isinstance(item, dict):
            yield item
        elif isinstance(item, list):
            yield from flatten(item)
```

# Example 2
Source: https://stackoverflow.com/a/6027615

```python
import collections

def flatten(d, parent_key='', sep='_'):
    items = []
    for k, v in d.items():
        new_key = parent_key + sep + k if parent_key else k
        if isinstance(v, collections.MutableMapping):
            items.extend(flatten(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)

>>> flatten({'a': 1, 'c': {'a': 2, 'b': {'x': 5, 'y' : 10}}, 'd': [1, 2, 3]})
{'a': 1, 'c_a': 2, 'c_b_x': 5, 'd': [1, 2, 3], 'c_b_y': 10}
```
