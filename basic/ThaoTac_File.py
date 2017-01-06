#Doc file
f = open('demo.txt', 'r')
str = f.read()

print('Noi dung file can doc:\n', str)

#Ghi file
info = \
    'Name: Mido Lê\n' + \
    'Mail: mido.uit@gmail.com\n' + \
    'Skype: mido93.uit'

f = open('demo_file2.txt', 'w')

f.write(info)

f.close()