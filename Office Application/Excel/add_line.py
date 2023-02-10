from openpyxl import Workbook

wb = Workbook() # 默认生成一个名为Sheet的sheet

# 创建sheet
for name in ['c','d']:

	ws = wb.create_sheet(name)

# 追加一行
for sheet in wb:
	sheet.append(['name','name2'])

# 在A列和B列追加(参数为字典)
for sheet in wb:
	sheet.append({'A':'dicta','B':'dictb'})

wb.save('test2.xlsx')