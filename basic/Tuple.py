#Khai bao : khi da khai bao thi khong thay doi gia tri, khong su dung dc ham append, pop

mytup = (1, 2, 3)
print(mytup)
print(type(mytup))

#Truy cap phan tu
print(mytup[0])
tuple = ('Mido', 12, 3.15, 'Stdio')

print(tuple[0])
print(tuple[1:3])
print(tuple[1:])
print(tuple[:2])
print(tuple[1::2])

#tuple long nhau
tuple = ('Mido', (12, 3.15), 'Stdio')

print (tuple[1])
print (tuple[1][1])

"""
Khác với lists, tuples không cho phép bạn thay đổi giá trị bên trong nó, kể cả độ dài của nó.
"""
#tuple[1] = 'Mido Lê'  #False

#do dai cua tuple
print(len(tuple))