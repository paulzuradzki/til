### Problem
Python datetime objects don't come with timezone info so we must add it.

### Solution
Python 3.9 has a new zoneinfo module in the standard library.
For <3.9, use a third-party library like pytz to "localize" the datetime object with the timezone of choice.

```python
import datetime
import pytz

# make a datetime object
dt = datetime.datetime.now()

# make a timezone object
local_tz = pytz.timezone('US/Central')

# "localize" the datetime object
dt_localized = local_tz.localize(dt)

# `%Z` format specifier is for timezone
dt_fmt = '%Y%m%d-%H:%M%Z'
dt_str = dt_localized.strftime(dt_fmt)

print(f"dt: {dt}")
print(f"dt_localized: {dt_localized}")
print(f"dt_str (formatted): {dt_str}")
```

### Output
```
dt: 2021-05-04 14:49:52.300886
dt_localized: 2021-05-04 14:49:52.300886-05:00
dt_str (formatted): 20210504-14:49CDT
```

