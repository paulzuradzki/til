# Today I Learned (TIL)
Here I log things I learn or code snippets that I keep forgetting.

### Categories
* [Python](#python)
* [SAS](#sas)
* [SQL](#sql)

---

### Python
- [OOP example](python/oop-demo.md)
- [OOP classes vs namedtuple](python/oop-namedtuple.py)
- [pandas - Concatenate strings from rows with GroupBy](python/pandas-concat-strings-from-rows-with-groupby.md)
- [Templating SQL from a Pandas dataframe](python/jinja-sql-template-from-dataframe.md)
- [Dictionary un-packing and how to set default and override configurations](python/dictionary-unpacking-for-configs.md)
- [Selecting data with df.query()](python/pandas-df-query.md)
- [Flatten a dictionary](python/flatten-dict.md)
- [Iterative vs. Recursive Processes with Factorial](python/recursion-factorial.md)
- [Method chaining by returning self](python/method-chaining.md)
- TODO: xlwings - read & write with Excel; split & merge sheets and workbooks
- TODO: matplotlib - subplots
- TODO: pandas pivoting methods and "named aggregations"
- TODO: pandas dataframe display in Jupyter
- TODO: use df.rename_axis(None, axis='columns').reset_index(drop=True) to manipulate index and axis name and remove multi-index
  - pivoted = pivoted['tripduration'].reset_index()
  - pivoted = pivoted.rename_axis(None, axis='columns').reset_index(drop=True)
 - [pivot non-numeric rows to x columns](python/pivot-non-numeric-to-x-fields.md)
 - [xlwings - add hyperlinks within a workbook](python/xl-add-hyperlinks-in-workbook.md)
 - [pandas - miscellaneous](python/pandas-misc.md)
 - [Heron's Method for Square Roots](python/square_root.md)
 - [Traverse file tree recursively](python/traverse-files.md)
 - [So You Want to Learn Python... (Python resource list)](python/so-you-want-to-learn-python.md)

### SAS
- [SAS Loops](sas/sas-loops.md)
- [Expand date spans to year-month view](sas/expand-dates.md)
- [Comparing terminology for similar concepts in Python and SAS](sas/sas-vs-python-semantics.md)
- [Disambiguating double ampersand and period in SAS macro variables](sas/sas-syntax-double&&-periods.md)
- [RSUBMIT and asynchronous SAS tasks](sas/rsubmit_async.md)
- TODO: importing CSVs

### SQL
- TODO: pivot, unpivot

### Editors
- [VS Code - configuration for Anaconda prompt](editors/vs-code/settings.json)
