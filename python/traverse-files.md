```python
# @author Paul Zuradzki

import os
from typing import List

def inventory_homemade(root_dir, inventory=None) -> List:
    '''Implements recursive file inventory function similar to os.walk().
    
    The local list variable `inventory` gets passed as an optional parameter in recursive call. 
    This prevents each recursive call from over-writing the inventory list variable 
    and avoids the need for a global list variable.
    '''
    inventory = [] if inventory is None else inventory
    for thing in os.listdir(root_dir):
        fpath = os.path.join(root_dir, thing)
        if os.path.isdir(fpath):
            inventory_homemade(fpath, inventory)
        inventory.append(fpath)
    return inventory

def inventory_os_walk(root_dir):
    '''Implementation of file inventory using os.walk() interface.'''
    inventory = []
    for root, dirs, files in os.walk(root_dir):
        for d in dirs:
            inventory.append(os.path.join(root, d))
        for f in files:
            fpath = os.path.join(root, f)
            inventory.append(fpath)
    return inventory

assert set(inventory_homemade('.')) == set(inventory_os_walk('.'))
```
