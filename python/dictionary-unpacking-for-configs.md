Dictionary un-packing and how to set default and override configurations

```python
import pprint
import yaml

yml_str = """

'defaults':
    'A': 'alpha orig'
    'B': 'beta orig'
    'C': 'charlie orig'

'sub':
    'A': 'alpha override '
    'C': 'charlie override'
    'D': 'delta new'
    'E': 'echo new'
"""
all_configs = yaml.safe_load(yml_str)

print('defaults:', all_configs['defaults'])
print('sub:', all_configs['sub'])


# copy default config and updates with child config parameters
# dictionary un-packing via PEP 448
config = {**all_configs['defaults'], **all_configs['sub']}
print('final:', config)
```
___
Output
```
defaults: {'A': 'alpha orig', 'B': 'beta orig', 'C': 'charlie orig'}
sub: {'A': 'alpha override ', 'C': 'charlie override', 'D': 'delta new', 'E': 'echo new'}
final: {'A': 'alpha override ', 'B': 'beta orig', 'C': 'charlie override', 'D': 'delta new', 'E': 'echo new'}
```

___
Also see Collections.ChainMap

```python
# hierarchical dictionary
# ChainMap lets you operate on multiple dicts as one

from collections import ChainMap

default = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
priority2 = {'a': 'one', 'b': 'two', 'c': 'three', 'd': 'four'}
priority1 = {'b': 'bee', 'c': 'see'}

lookup = ChainMap(priority1, priority2, default)

for x in 'abcde':
    print("{}: {}".format(x, lookup[x]))
```
___
Output
```
a: one
b: bee
c: see
d: four
e: 5
```
