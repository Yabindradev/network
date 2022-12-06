import socket
try:
    c = socket.socket()
    
    c.connect(('localhost', 1111))
    name = input("Username: ")
    c.send(bytes(name, 'utf-8'))
    print(c.recv(1024).decode())
    
    while True:
       message = input("message :")
       c.send(bytes(message, 'utf-8'))
       print(c.recv(1025).decode())
except:
    print("Server si not ready for connection")