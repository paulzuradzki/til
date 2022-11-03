# Problem
Issue: Sometimes, our data has multiple row offsets within the same workbook.
* The skiprows param in pd.read_excel(sheet_name=None, skiprows=some_number)  gets applied to all sheets.
* You use a lower level pd.ExcelFile() object to do custom parsing on each sheet. 
* This also keeps the file handler open so it works better than trying to call pd.read_csv() multiple times too if you have many sheets


# Solution

### Set up demo
```python
import pandas as pd
import seaborn as sns

df = sns.load_dataset('mpg')

car_origins = df['origin'].unique().tolist()
print(f"car_origins: {car_origins}")

xl_filepath = "pandas_excel_multiple_sheets_demo.xlsx"

# write data
with pd.ExcelWriter(xl_filepath, mode='w', engine='openpyxl') as writer:
    df.query("origin=='usa'").to_excel(writer, sheet_name='usa', index=False, startrow=0)
    df.query("origin=='japan'").to_excel(writer, sheet_name='japan', index=False, startrow=2)
    df.query("origin=='europe'").to_excel(writer, sheet_name='europe', index=False, startrow=4)
```

### Read our file back

### Option 1 - `pd.read_excel(filepath, sheet_name=None)`
* most common yet still not super well-known
* You can pass `sheet_name=None` to `pd.read_excel()`
* Which will return a dictionary of dataframes rather than a single dataframe
* Each key is a sheet_name
* Problem: applies same parameters to each sheet

### Option 2 - use `pd.ExcelFile()` object directly
* This is lower-level but gives finer control where you can parse each sheet with different parameters as needed
* It's super handy especially since many workbooks have datasets in tabs with different offsets
* Had we used `pd.read_excel(sheet_name=None)`, we would not be able to customize the `skiprow` argument

```python
import pandas as pd

xl_filepath = "pandas_excel_multiple_sheets_demo.xlsx"

df_all = pd.DataFrame()
with pd.ExcelFile(xl_filepath) as xl_fileobj:
    df1 = xl_fileobj.parse(sheet_name='usa', skiprows=0)
    df2 = xl_fileobj.parse(sheet_name='japan', skiprows=2)
    df3 = xl_fileobj.parse(sheet_name='europe', skiprows=4)
    df_all = pd.concat([df1, df2, df3])


# all_dfs_dict = pd.read_excel(xl_filepath, sheet_name=None)
# ^^^ won't always work with multiple offsets in same file
```

### References
* https://pythoninoffice.com/read-multiple-excel-sheets-with-python-pandas/
