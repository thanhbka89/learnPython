#Khai bao chuoi

str1 = "Hello"
str2 = 'World'

#Khai bao chuoi tren nhieu dong su dung dau """
paragrap = """
Toi la Thanhnm
Den tu Ha Noi
Dang lam culi
"""

#truy xuat ki tu trong chuoi
print(str1[0])
print(paragrap)

#Noi chuoi
s = str1 + ' ' + str2
print(s)

#Trich xuat chuoi con
print(s[0 : 4])
print(len(s))

#replace
s1 = s.replace('Hello', "BYE")
print(s1)

#Tim vi tri chuoi con : co phan biet chu hoa chu thuong
print("Vi chi chuoi con : ", s.find('world'))
print("Vi chi chuoi con : ", s.find('World'))

#Tach chuoi
chuoicon = s.split(' ');
print(chuoicon)
print(type(chuoicon))

#unicode
s = 'sky no enemy'
print(type(s),len(s))

s = 'nguyễn thành mai'
print(type(s),len(s))
print(s)

print('UNICODE')
s = u"nguyễn thành mai"
s = s.encode('utf8')
print(type(s),len(s))
print(s)
i = 0
for x in s:
    print(x)
print(type(u""))
