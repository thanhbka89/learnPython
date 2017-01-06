#Dinh nghia ham
#Neu ham khong tra ve du lieu thi mac dinh tra ve NONE

def showInfo(info):
    print(info)

def add(a, b):
    return a + b

#Goi ham
print(showInfo('thanhbka'))

print('=============================')
print(add(3, 4))
print(add('Mido ', 'Lê'))


#Ham voi tham so mac dinh
def TinhTong(num1, num2, num3=0, num4=0):
    return (num1 + num2 + num3 + num4)


print('Tong 4 so: ', TinhTong(3, 4, 2, 1))
print('Tong 3 so: ', TinhTong(3, 4, 2))
print('Tong 2 so: ', TinhTong(3, 4))

#Tham so su dung tu khoa
def printInfomation(name='Mido Lê', mail='mido.uit@gmail.com', skype='mido93.uit'):
    info = \
        'Name: ' + name + '\n' + \
        'Mail: ' + mail + '\n' + \
        'Skype: ' + skype
    print(info)


printInfomation(mail='mido.le@stdio.vn')

