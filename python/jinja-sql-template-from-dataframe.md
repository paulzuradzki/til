Code
----
```python

from jinja2 import Template
import pandas as pd

# starting with dataframe
mapping_df = pd.DataFrame([['ALABAMA', 'AL'], ['ALASKA', 'AK'], ['ARIZONA', 'AZ'], ['ARKANSAS', 'AR'], ['CALIFORNIA', 'CA'], ['COLORADO', 'CO'], ['CONNECTICUT', 'CT'], ['DELAWARE', 'DE'], ['FLORIDA', 'FL'], ['GEORGIA', 'GA'], ['HAWAII', 'HI'], ['IDAHO', 'ID'], ['ILLINOIS', 'IL'], ['INDIANA', 'IN'], ['IOWA', 'IA'], ['KANSAS', 'KS'], ['KENTUCKY', 'KY'], ['LOUISIANA', 'LA'], ['MAINE', 'ME'], ['MARYLAND', 'MD'], ['MASSACHUSETTS', 'MA'], ['MICHIGAN', 'MI'], ['MINNESOTA', 'MN'], ['MISSISSIPPI', 'MS'], ['MISSOURI', 'MO'], ['MONTANA', 'MT'], ['NEBRASKA', 'NE'], ['NEVADA', 'NV'], ['NEW HAMPSHIRE', 'NH'], ['NEW JERSEY', 'NJ'], ['NEW MEXICO', 'NM'], ['NEW YORK', 'NY'], ['NORTH CAROLINA', 'NC'], ['NORTH DAKOTA', 'ND'], ['OHIO', 'OH'], ['OKLAHOMA', 'OK'], ['OREGON', 'OR'], ['PENNSYLVANIA', 'PA'], ['RHODE ISLAND', 'RI'], ['SOUTH CAROLINA', 'SC'], ['SOUTH DAKOTA', 'SD'], ['TENNESSEE', 'TN'], ['TEXAS', 'TX'], ['UTAH', 'UT'], ['VERMONT', 'VT'], ['VIRGINIA', 'VA'], ['WASHINGTON', 'WA'], ['WEST VIRGINIA', 'WV'], ['WISCONSIN', 'WI'], ['WYOMING', 'WY']],
            columns=['state', 'abbr'])

print('data:')
print(mapping_df.head().to_markdown(), '\n')

# convert back to list of lists
# [['ALABAMA', 'AL'], ['ALASKA', 'AK'], ['ARIZONA', 'AZ'], ...
mapping_lol = mapping_df.head().values.tolist()

# make jinja template with for loop
sql_template = """
select
{%- for row in data %}
    when state like '%, {{ row[1] }}' then '{{ row[0] }}' end as state_name
{%- endfor %}
from table
"""

# render sql
sql = Template(sql_template).render(data=mapping_lol)

print('rendered sql with data parameters:')
print(sql)
```

Output
------
```
data:
|    | state      | abbr   |
|---:|:-----------|:-------|
|  0 | ALABAMA    | AL     |
|  1 | ALASKA     | AK     |
|  2 | ARIZONA    | AZ     |
|  3 | ARKANSAS   | AR     |
|  4 | CALIFORNIA | CA     | 

rendered sql with data parameters:

select
    when state like '%, AL' then 'ALABAMA' end as state_name
    when state like '%, AK' then 'ALASKA' end as state_name
    when state like '%, AZ' then 'ARIZONA' end as state_name
    when state like '%, AR' then 'ARKANSAS' end as state_name
    when state like '%, CA' then 'CALIFORNIA' end as state_name
from table
```
