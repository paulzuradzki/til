```python

# The trick is to use the filename plus `#` symbol before the Sheet!cell address
# This is handy for a Table of Contents worksheet that links to other tabs and back

import xlwings as xw

wb = xw.Book()
wb.save('my_workbook.xlsx')
sheetname = 'Sheet1'
wb.sheets.add('TOC')
wb.sheets['TOC'].range('A2').add_hyperlink(address=f'my_workbook.xlsx#{sheetname}!A1', 
                                           text_to_display=f'Jump to {sheetname}')
wb.save()
```
