How to export to Excel from SAS

```sas
proc export data=a_table
  outfile='/foo/bar/folder_path/deliverable.xlsx'
  dbms=xlsx replace;
run;
```
