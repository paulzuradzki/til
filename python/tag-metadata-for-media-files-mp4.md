# Problem

I want to extra metadata from a media files, so I can estimate total duration across several video files.

# Solution

Use `tinytag` library to get the minimum necessary metadata.

Most of the code in the example below is analytical Python/pandas.
__

### Tiny Tag Usage

```python
from tinytag import TinyTag

tag = TinyTag.get({SOME_FILE_PATH}).as_dict()
print(tag)
```

```
   {'filesize': 24477531, 'album': None, 'albumartist': None, 
    'artist': None, 'audio_offset': None, 'bitrate': 128.002, 
    'channels': 2, 'comment': None, 'composer': None, 'disc': None, 
    'disc_total': None, 'duration': 835.395, 'genre': None, 
    'samplerate': 44100, 'title': None, 'track': None, 'track_total': None, 
    'year': None, 'course': 'text-mining'}
```

### Analysis

```python

"""mp4-meta

Use tinytag library to extract metadata from mp4 video files.

"""

from tinytag import TinyTag
from pathlib import Path
import os
import pandas as pd
pd.set_option('max_colwidth', None)

BASE_DIR = Path('') # add file path to scan

# build metadata dictionary for mp4 files by scanning all mp4s in the directory and sub-dirs
data = {}
for root, dirs, files in os.walk(BASE_DIR):
    for f in files:
        if f.endswith('.mp4'):
            filepath = os.path.join(root, f)
            tag = TinyTag.get(filepath).as_dict()
            
            # build data dict
            data[f] = tag
            data[f]['course'] = filepath.split('/')[5]
            
df = (pd.DataFrame(data)                    # read data from dict
        .T                                  # transpose
        .dropna(axis=1)                     # drop empty columns with None values
        .rename_axis('filename')            # give index a name (keys from original dict)
        .reset_index()                      # bring out index as column
        .loc[:, ['filename', 'course', 'filesize', 'duration']] # limit columns
     )

df['duration_min'] = (df['duration'] / 60).astype('float')
df['duration_hr'] = (df['duration_min'] / 60).astype('float')
```

### Example Output

```python
df.head()
```
|    | filename                                           | course                                   |   filesize |   duration |   duration_min |   duration_hr |
|---:|:---------------------------------------------------|:-----------------------------------------|-----------:|-----------:|---------------:|--------------:|
|  0 | 01_welcome-to-3d-scientific-data-visualization.mp4 | data-visualization-science-communication |   35327466 |    174.404 |        2.90673 |     0.0484456 |
|  1 | 01_closing.mp4                                     | data-visualization-science-communication |    6270505 |     78.063 |        1.30105 |     0.0216842 |
|  2 | 02_transformations-and-attributes.mp4              | data-visualization-science-communication |   38186854 |    387.738 |        6.4623  |     0.107705  |
|  3 | 01_software.mp4                                    | data-visualization-science-communication |   41375378 |    466.159 |        7.76932 |     0.129489  |
|  4 | 03_programming.mp4                                 | data-visualization-science-communication |   40233312 |    555.951 |        9.26585 |     0.154431  |


```python
df.groupby(['course']).agg({'duration_hr': 'sum'})
```
| course                                   |   duration_hr |
|:-----------------------------------------|--------------:|
| cloud-applications-part1                 |     10.5342   |
| cloud-applications-part2                 |     13.7971   |
| cloud-computing                          |      8.8104   |
| cloud-computing-2                        |      6.64515  |
| cloud-computing-project                  |      0.113341 |
| cloud-networking                         |      8.26738  |
| cluster-analysis                         |      4.22835  |
| cs-fundamentals-1                        |      2.95362  |
| cs-fundamentals-2                        |      3.03048  |
| cs-fundamentals-3                        |      3.09812  |
| data-patterns                            |      4.18681  |
| data-visualization-science-communication |      5.19951  |
| datavisualization                        |      5.71523  |
| iot-cloud                                |      2.62447  |
| iot-communications                       |      6.63311  |
| iot-devices                              |      2.09545  |
| iot-networking                           |      4.14169  |
| text-mining                              |     12.0792   |
| text-retrieval                           |      9.4105   |
