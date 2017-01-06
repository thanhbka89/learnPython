#khai bao
point = {'x':1, 'y':2}
print(point)
print(type(point))

#truy xuat dua vao key
print(point['x'])

#them phan tu
point['z'] = 3
print(point)

#cap nhat key
point['x'] = 1000
print(point)

#xoa toan bo du lieu
#point.clear()
#print(point)

#xoa phan tu
del  point['y']
print(point)

#xoa bien kieu dict
#del point
#print(point)

#So phan tu trong dict
print(len(point))

#copy
dic2 = point.copy()
print(dic2)
dic2['x'] = 999

#Them cac phan tu dic2 vao dic1
point.update(dic2)
print(point)

#kiem tra key co ton tai

#tra ve key
print(point.keys())
print(point.values())
