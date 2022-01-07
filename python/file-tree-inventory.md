Utilies for gathering metadata on files and file trees.

```python
from datetime import datetime
import os
from pathlib import Path
import win32security
import pandas as pd

def get_file_owner(filepath):
    """Use win32 API to get file owner in 'domain/username' format for Windows."""
    owner_sid = win32security.GetFileSecurity(filepath, win32security.OWNER_SECURITY_INFORMATION).GetSecurityDescriptorOwner()
    name, domain, _type = win32security.LookupAccountSid(None, owner_sid)
    return f'{domain}/{name}'

def get_file_stats(filepath):
    """Return a dictionary of file properties."""
    filepath = Path(filepath)
    stats = os.stat(filepath)

    file_stats = {
        'path': filepath,
        'name': filepath.name,
        'parent': filepath.parent,
        'size_mb': round(stats.st_size / 1024**2, 4),
        'modified_dt': datetime.fromtimestamp(stats.st_mtime).strftime('%Y.%m.%d-%H%M'),
        'create_dt': datetime.fromtimestamp(stats.st_ctime).strftime('%Y.%m.%d-%H%M'),
        'owner': get_file_owner(str(filepath)),
        'is_file': int(filepath.is_file()),
        'is_dir': int(filepath.is_dir()), 
    }
    return file_stats

def make_file_inventory(root_dir: Path, as_df=False):    
    """Return a dictionary or dataframe of file attributes for a file tree."""
    inventory = []

    for root, dirs, files in os.walk(root_dir):
        for f in files:
            filepath = Path(root) / f
            inventory.append(get_file_stats(filepath))
        for d in dirs:
            dirpath = Path(root) / d
            inventory.append(get_file_stats(dirpath))
            
    if as_df:
        return pd.DataFrame(inventory).sort_values(by=['is_file', 'path'])
    
    return inventory
```

Example output of get_file_stats(path)
```
{'create_dt': '2022.01.06-1950',
 'is_dir': 1,
 'is_file': 0,
 'modified_dt': '2022.01.06-1950',
 'name': 'dir_01',
 'owner': 'domain/PZuradzki',
 'parent': WindowsPath('root'),
 'path': WindowsPath('root/dir_01'),
 'size_mb': 0.0039}
```
Example output of make_file_inventory(path)
```
| path                  | name      | parent      |   size_mb | modified_dt     | create_dt       | owner            |   is_file |   is_dir |
|:----------------------|:----------|:------------|----------:|:----------------|:----------------|:-----------------|----------:|---------:|
| root\dir_01           | dir_01    | root        |    0.0039 | 2022.01.06-1950 | 2022.01.06-1950 | domain/PZuradzki |         0 |        1 |
| root\dir_01\subdir_01 | subdir_01 | root\dir_01 |    0      | 2022.01.06-1950 | 2022.01.06-1950 | domain/PZuradzki |         0 |        1 |
| root\dir_01\subdir_02 | subdir_02 | root\dir_01 |    0      | 2022.01.06-1950 | 2022.01.06-1950 | domain/PZuradzki |         0 |        1 |
| root\dir_01\subdir_03 | subdir_03 | root\dir_01 |    0      | 2022.01.06-1950 | 2022.01.06-1950 | domain/PZuradzki |         0 |        1 |
| root\dir_02           | dir_02    | root        |    0.0039 | 2022.01.06-1950 | 2022.01.06-1950 | domain/PZuradzki |         0 |        1 |
| root\dir_02\subdir_01 | subdir_01 | root\dir_02 |    0      | 2022.01.06-1950 | 2022.01.06-1950 | domain/PZuradzki |         0 |        1 |
| root\dir_02\subdir_02 | subdir_02 | root\dir_02 |    0      | 2022.01.06-1950 | 2022.01.06-1950 | domain/PZuradzki |         0 |        1 |
| root\dir_02\subdir_03 | subdir_03 | root\dir_02 |    0      | 2022.01.06-1950 | 2022.01.06-1950 | domain/PZuradzki |         0 |        1 |
| root\dir_03           | dir_03    | root        |    0.0039 | 2022.01.06-1950 | 2022.01.06-1950 | domain/PZuradzki |         0 |        1 |
| root\dir_03\subdir_01 | subdir_01 | root\dir_03 |    0      | 2022.01.06-1950 | 2022.01.06-1950 | domain/PZuradzki |         0 |        1 |
```
