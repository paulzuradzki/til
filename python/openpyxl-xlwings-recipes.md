# Automating Excel using `pandas`+`openpyxl` or `pandas`+`xlwings`

This snippet shows common write operations like:
* copy/paste pandas dataframes from Python pandas to Excel 
* apply autofit column width formatting
* apply basic font styling

The operations are shown using both openpyxl and xlwings to compare the APIs.

### Reference Links
* https://xlsxwriter.readthedocs.io/
* https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_excel.html 
* https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.ExcelWriter.html#pandas.ExcelWriter
* https://xlsxwriter.readthedocs.io/alternatives.html
* https://www.python-excel.org/

### Notes on Python Excel libraries
openpyxl
* supports read and write
* good lightweight default

xlsxwriter
* cannot modify existing workbook; can only write to workbook; 
* supports workbooks with charts and images

xlwings
* nice API
  * built-in pandas df copy/paste
  * built-in auto-fit column width
* cons: 
    * requires opening application instance; makes it harder to deploy on a server
    * this also may reduce performance
* supports Excel Add-Ins; calling Python from Excel and vice versa

xlrd
* used for older .xls format

lxml
* this is a Python xml handling library
* lmxl is necessary for openpyxl if you want to use the optimized "write-only" mode. 


# Demonstrations
* both implementations take two pandas dataframes 'iris' and 'mpg' (imported from seaborn) and paste them into Excel sheets of a workbook
* autofit column width is applie
* a title cell is added and style

## openpyxl implementation
* notice the need to handroll a "_columns_best_fit" function
* notice the use of pandas ExcelWriter to paste the dataframes
* in xlwings, these come built-in
* fonts/styling seems 

```python
import openpyxl
from openpyxl.styles import Font #P atternFill, Border, Side, Alignment, Protection, 
import seaborn as sns
import pandas as pd

def openpyxl_demo():

    def _columns_best_fit(ws: openpyxl.worksheet.worksheet.Worksheet):
        """Make all columns best fit."""
        column_letters = tuple(openpyxl.utils.get_column_letter(col_number + 1) for col_number in range(ws.max_column))
        for column_letter in column_letters:
            dim = openpyxl.worksheet.dimensions.ColumnDimension(ws, index=column_letter, bestFit=True)
            ws.column_dimensions[column_letter] = dim
    
    # load data to pandas
    df1 = sns.load_dataset('iris')
    df2 = sns.load_dataset('mpg')
    
    # create new Excel file and export df's to separate sheets 
    xl_filename = "pandas_excel_demo_01.xlsx"
    with pd.ExcelWriter(xl_filename, mode='w', engine='openpyxl') as writer:
        df1.to_excel(writer, sheet_name="iris" , index=False, startrow=3, startcol=1)
        df2.to_excel(writer, sheet_name="mpg", index=False, startrow=3, startcol=1)

    
    # reload workbook
    wb = openpyxl.load_workbook(xl_filename)    
    
    # autofit column width for worksheet
    _columns_best_fit(wb['iris'])
    _columns_best_fit(wb['mpg'])

    # update value and font in cell A1
    fnt = Font(name='Calibri', size=16, bold=True, italic=False, 
               vertAlign=None, underline='none', strike=False, color='FF000000')
    wb['iris']['A1'].value = 'Iris Data'
    wb['iris']['A1'].font = fnt 

    wb['mpg']['A1'].value = 'MPG Data'
    wb['mpg']['A1'].font = fnt 

    wb.save(xl_filename)
    wb.close()
```

## xlwings implementation
```python
import xlwings as xw
import seaborn as sns
import pandas as pd

def xlwings_demo():

    # used later in save step
    xl_filename = 'pandas_excel_demo_02.xlsx'

    # load data to pandas
    df1 = sns.load_dataset('iris')
    df2 = sns.load_dataset('mpg')

    # init new workbook
    wb = xw.Book()

    # function to preview sheets before and after edits
    print_sheets = lambda: print([sht.name for sht in wb.sheets])

    # add two new sheets and delete original 'Sheet1' (-1 index after additions)
    print_sheets()
    wb.sheets.add('iris')
    wb.sheets.add('mpg')
    wb.sheets[-1].delete()
    print_sheets()

    # paste the pandas data frames using "without index" option
    wb.sheets['iris']['B3'].options(pd.DataFrame, index=False).value = df1
    wb.sheets['mpg']['B3'].options(pd.DataFrame, index=False).value = df2

    wb.sheets['iris']['B1'].value = 'Iris Data'
    wb.sheets['mpg']['B1'].value = 'MPG Data'

    # formatting for each sheet
    for sheet_name in ['iris', 'mpg']:

        # font formatting
        wb.sheets[sheet_name]['B1'].font.name = 'calibri'
        wb.sheets[sheet_name]['B1'].font.bold = True
        wb.sheets[sheet_name]['B1'].font.size = 16
        wb.sheets[sheet_name]['B1'].font.color = (255, 0, 0) # red

        # autofit columns
        wb.sheets[sheet_name].autofit('c')

    wb.save(xl_filename)
    wb.close()
```
