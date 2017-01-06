print("Xin chao moi nguoi. Hello World!")

#Kieu du lieu
z = 2 + 3j #So phuc
print(z.real)
t=True #bool
print(t)
s='thanhnm'
x = 5
y= 7.4

#Bien : ko can khai bao kieu
print(type(x))
print(type(y))
print(type(t))
print(type(z))
print(type(s))

#Xoa bien : Neu bien do dang ton tai, xoa di thi khong su dung duoc nua
#del s
#print(s)

#Kiem tra vung luu tru gia tri cua cac bien int float
import sys
print(sys.int_info)

"""
Ghi chu nhieu dong
"""

#Toan tu so hoc
print("chia lay phan du")
print(9%4)
print("Chia lay phan nguyen")
print(9//4)
print("luy thua")
print(2**3) #2^3

#Toan tu so sanh
x=5
y=5
print(x is y) #Tra ve True neu 2 bien cung tro den 1 doi tuong (hoac cung gia tri)

#Toan tu logic
if (not x>=5):
    print("Ngắm gà khỏa thân và nải chuối")
else:
    print("Đậu")

#Toan tu ton tai : in ; not in
print("Su dung toan tu IN:", 'good' in	'this is a greate example')

#Xuat du lieu tren cung 1 dong
print("Obama",end=' ')
print("Xin chào",end=' ')
print("Putin")

#Danh sach
a = ['spam', 'eggs', 100, 1234]
print(a)
print(len(a))

#Khoi lenh : Cac lenh lien tiep co cung khoang cach thut dau dong
if True:
       print ("Answer")
       print ("True")
else:
       print ("Answer")
print ("False")
var = 100
if var == 200:
    print("1 - Got a true expression value")
elif var == 100:
    print("3 - Got a true expression value")
else:
    print("4 - Got a false expression value")

print("Good bye!")

print(range(9))
