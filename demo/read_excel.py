import xlrd

print(xlrd.__file__)
print(dir(xlrd))

print(dir())
file_location = 'demo.xlsx'
wb = xlrd.open_workbook(file_location)
sheet = wb.sheet_by_index(0)
print (sheet.nrows)
print (sheet.ncols)
print (sheet.cell_value(3, 1)) #Giá trị tại vị trí dòng 3+1 cột 1+1. Tức vị trí B4 trong bảng tính

# in ra tất cả các giá trị của cột đầu tiên
for rows in range(sheet.nrows):
    data = sheet.cell_value(rows, 0)
    print (data, end=' ')
print('')
#In gia tri dong dau tien
for col in range(sheet.ncols):
	print (sheet.cell_value(0, col), end=' ')

#Lay toan bo du lieu bang
data = [[sheet.cell_value(r, c) for c in range(sheet.ncols)] for r in range(sheet.nrows)]
print(data)
print(type(data))