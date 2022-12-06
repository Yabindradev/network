import socket

s = socket.socket()
print('Socket Connection')

s.bind(('localhost', 1111))
s.listen(3)
print(" Waiting for connection")

while True:
    c, addr = s.accept()
    name = c.recv(1024).decode()
    print(name," is connection with", addr)
    c.send(bytes("Welocme to chat group", 'utf-8'))

    message = c.recv(1025).decode()
    c.send(bytes("sucesfuly reciver your messages", 'utf-8'))
    print(name ,":", message)
    c.close()