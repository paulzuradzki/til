# Problem
Filling forms using PyPDF2's out-of-the-box updatePageFormFieldValues leads to a glitch in some templates where the field data does not appear in the output unless a user clicks on the field.

# Solution
Here we use a _set_need_appearances_writer() helper function to modify the PDF writer object's "acroform" properties to make the field values visible.

Source: https://github.com/mstamy2/PyPDF2/issues/355

```python

from pprint import pprint
import os
from PyPDF2 import PdfFileReader, PdfFileWriter
from PyPDF2.generic import BooleanObject, NameObject, IndirectObject
from typing import Dict

def fill_form(source_filepath, destination_filepath, field_data: Dict):
    """
    Fills PDF form template with template to new file. Template PDF must have fields pre-defined.
    
    Parameters
    ----------
    source_filepath
    destination_filepath
    field_data: dictionary of field_name: value pairs
    
    """
    
    # initialize the input (reader) and filled/output (writer) PDF objects
    input_pdf = PdfFileReader(source_filepath)
    filled_pdf = PdfFileWriter()
    
    # special edit to output PDF to fix issue with field data not appearing unless user clicks on field
    # reference: https://github.com/mstamy2/PyPDF2/issues/355
    filled_pdf = _set_need_appearances_writer(filled_pdf)
    
    # copy first page from template
    filled_pdf.addPage(input_pdf.getPage(0))
    
    # fill fields
    filled_pdf.updatePageFormFieldValues(page=filled_pdf.getPage(0), fields=field_data)

    # write out file
    with open(destination_filepath, 'wb') as f:
        filled_pdf.write(f)
        
def _set_need_appearances_writer(writer: PdfFileWriter):
    # See 12.7.2 and 7.7.2 for more information: http://www.adobe.com/content/dam/acom/en/devnet/acrobat/pdfs/PDF32000_2008.pdf
    try:
        catalog = writer._root_object
        # get the AcroForm tree
        if "/AcroForm" not in catalog:
            writer._root_object.update({
                NameObject("/AcroForm"): IndirectObject(len(writer._objects), 0, writer)})

        need_appearances = NameObject("/NeedAppearances")
        writer._root_object["/AcroForm"][need_appearances] = BooleanObject(True)
        return writer

    except Exception as e:
        print('set_need_appearances_writer() catch : ', repr(e))
        return writer


# get field names from template form (if not known in advance)
# designer with Acrobat can also view these
pdf_dir = r'C:\Users\...\templates'
source_filepath = os.path.join(pdf_dir, 'Template.pdf')

with open(source_filepath, 'rb') as f:
    pdf = PdfFileReader(f)
    info = pdf.getDocumentInfo()
    n_pages = pdf.getNumPages()
    form_text_field_names = list(pdf.getFormTextFields().keys())

print("number pages:", n_pages)

print("="*10, "Fields:", "="*10, sep="\n")
for field in form_text_field_names: 
    print(field)

# fill form
pdf_dir = r'C:\Users\...\templates'
source_filepath = os.path.join(pdf_dir, 'Template.pdf')
destination_filepath = os.path.join(pdf_dir, 'filled_form_dev.pdf')

field_data = {'Member Name (Last, First)': 'Foo Bar', 
              'DOB': '1/1/1900'}

fill_form(source_filepath, destination_filepath, field_data)
```

