from openpyxl import Workbook

wb = Workbook() # 默认生成一个名为Sheet的sheet

# 创建sheet
for name in ['a','b']:
	ws = wb.create_sheet(name)

# 追加一行
for sheet in wb:
	sheet.append(['name'])

# 第一行插入空行
for sheet in wb:
	sheet.insert_rows(1)

# 在第2行往下数3行插入空行(2、3、4行)
for sheet in wb:	
	sheet.insert_rows(2,3)

wb.save('test3.xlsx')