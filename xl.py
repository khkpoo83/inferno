import openpyxl

def write_xl(filename,sheetname,contents):
    xl=openpyxl.Workbook()
    xl_sheet=xl.active
    xl_sheet.name=sheetname
    for row in contents:
        xl_sheet.append(row)
    xl.save(filename)
    xl.close()