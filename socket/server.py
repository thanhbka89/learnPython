import socket

print(socket.__file__)
print(dir(socket))

s = socket.socket()
host = socket.gethostname()
print(host)
port = 12345
s.bind((host, port))

s.listen(5)
while True:
    c, addr = s.accept()
    print('Got connection from', str(addr))
    msg = 'Thank you for connecting' + "\r\n"
    c.send(msg.encode('ascii'))
    c.close()