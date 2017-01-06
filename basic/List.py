"""
Ngoài điểm khác nhau nêu trên giữa Lists và Tuples thì còn một điểm khác nhau lớn nữa đó là: Các phần tử và độ lớn của Lists có thể cập nhật nhưng với Tuples thì không.
Gia tri cac phan tu co the trung nhau
"""
#Khai bao

numbers = [1, 2, 3, 4, 5, 6]
names = ['thanh', 'thoan', 'hieu']

#truy xuat
print(numbers[1])
print(numbers[-4])

list = ['Mido', 12, 3.15, 'Stdio']
print(list[0])
print(list[1:3])
print(list[1:])
print(list[:2])
print(list[1::2])

#Kiem tra phan tu ton tai
#Kiem tra theo Index
index = 3
#Look before you leap
if index < len(numbers):
    print(numbers[index])
else:
    print('Out index')

#Easier	to	ask	forgiveness	than permission
try:
    print(numbers[index])
except IndexError:
    print('Error')

#Kiem tra theo Gia tri
print('thanh' in names)

#Trich xuat mang con
print(numbers[2:5])

#Xoa phan tu mang
del numbers[0]
print(numbers)

#Noi mang
a = [1, 2]
b = [3, 4]
c = a + b
print(c)

# Them phan tu vao cuoi mang
c.append(5)
print(c)

#Lay phan tu cuoi mang : tra ve phan tu cuoi cung cua mang và mang ko con chua phan tu da lay
print(c.pop())
print(c)

#Tim gia tri trong mang
print(c.index(4))

#Dao nguoc gia tri mang
c.reverse()
print(c)

#cap nhat
list[0] = 'Mido Lê'
print(list[0])

#list trong list
list = ['Mido', [1, 2, 3], 'Stdio']

print(list[1])
print(list[1][2])

#Do dai (so luong phan tu) trong líst
print(len(list))

#them phan tu vao vi tri bat ky
list.insert(2, 'Mido')
print(list)

