### Description
Use `zipfile.ZipFile(io.BytesIO(response))` to read zipfile bytes and call pd.read_csv() on a specific file. This method is not necessary if the zipfile URL has only one text file. In that case, you can call pd.read_csv() directly on the URL.

### Code
```python
import zipfile
from zipfile import ZipFile
import io
from urllib.request import urlopen
import pandas as pd

r = urlopen("https://www.cms.gov/Medicare/Medicare-Fee-for-Service-Payment/AcuteInpatientPPS/Downloads/FY_2010_FR_Table_5.zip").read()

with ZipFile(io.BytesIO(r)) as zf:
    print('ZIP contents:', zf.namelist())
    drg_lookup_df = (
        pd.read_csv(zf.open('FY 2010 FR Table 5.txt'), sep='\t')
          .dropna(subset=['FY 2010 Final Rule Post-Acute DRG'])         
          .pipe(lambda _df: _df.rename(columns={col: col.strip().replace(' ', '_').replace('-', '').lower() for col in _df.columns}))
    )
    
print(drg_lookup_df.head().to_markdown(index=False))
```

### Output
ZIP contents: ['FY 2010 FR Table 5.txt', 'FY 2010 FR Table 5.xls']
|   msdrg | fy_2010_final_rule_postacute_drg   | fy_2010_final_rule_special_pay_drg   | mdc   | type   | msdrg_title                                                         |   weights |   geometric_mean_los |   arithmetic_mean_los |
|--------:|:-----------------------------------|:-------------------------------------|:------|:-------|:--------------------------------------------------------------------|----------:|---------------------:|----------------------:|
|     001 | No                                 | No                                   | PRE   | SURG   | HEART TRANSPLANT OR IMPLANT OF HEART ASSIST SYSTEM W MCC            |   24.8548 |                 31.5 |                  43.9 |
|     002 | No                                 | No                                   | PRE   | SURG   | HEART TRANSPLANT OR IMPLANT OF HEART ASSIST SYSTEM W/O MCC          |   11.754  |                 16.4 |                  21.2 |
|     003 | Yes                                | No                                   | PRE   | SURG   | ECMO OR TRACH W MV 96+ HRS OR PDX EXC FACE, MOUTH & NECK W MAJ O.R. |   18.2667 |                 31.6 |                  38.5 |
|     004 | Yes                                | No                                   | PRE   | SURG   | TRACH W MV 96+ HRS OR PDX EXC FACE, MOUTH & NECK W/O MAJ O.R.       |   11.1941 |                 22.9 |                  28.2 |
|     005 | No                                 | No                                   | PRE   | SURG   | LIVER TRANSPLANT W MCC OR INTESTINAL TRANSPLANT                     |   10.1358 |                 14.9 |                  20.3 |
