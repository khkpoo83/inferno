import openpyxl

def init_xl(sheetname):
    xl=openpyxl.Workbook()
    xl_sheet=xl.active
    xl_sheet.title = sheetname
def set_header(header):
    xl_sheet.append(header)

def write_xl(filename,contents):
    for row in contents:
        xl_sheet.append(row)
    xl.save(filename)
    xl.close()