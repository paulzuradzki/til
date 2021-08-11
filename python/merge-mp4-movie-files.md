# Problem
I have several smaller `mp4` video files in directories and sub-directories. I would like to view these clips as one longer file.

In this case, the files can be sorted properly by filename for the merged clip to play in the correct order.

# Solution
* Walk the directory and collect all mp4s
* Use `moviepy.editor` library
  * me.VideoClip() to instantatiate video object
  * me.concatenate_videoclips(List) to merge
  * me.VideoClip().write_videofile() for output

```python

import moviepy.editor as me
from typing import List

base_dir = Path('') # EDIT: user to add path

# build list of filepaths for mp4 files by scanning directory and sub-dirs
filepaths: List[tuple] = []
for root, dirs, files in os.walk(base_dir):
    for f in files:
        if f.endswith('.mp4'):
            filepath = os.path.join(root, f)
            filepaths.append((f, filepath))

# filepaths list of tuples is in form of (filename, filepath)
# we will use the filename for sort order for final movie clip
filepaths = sorted(filepaths, key=lambda x: x[0])

# generate list of video clips, merge, export
videos = [me.VideoFileClip(fp)for f, fp in filepaths]
final_video = me.concatenate_videoclips(videos)
final_video.write_videofile("./output.mp4")
```
