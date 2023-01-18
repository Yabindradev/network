#
# tcp_client.py
#
import sys
import socket
import select


try:
    tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_client_socket.connect(('127.0.0.1', 8888))

    name = input("Username: ")
    tcp_client_socket.send(bytes(name, 'utf-8'))


except Exception:
    print('Server is not ready to connection')
else:
    while True:
        error = tcp_client_socket.recv(1025).decode()
        if error == "username is invalid":
            print(error)
            break
        else:
            while True:
                msg = input('message:  ')
                tcp_client_socket.send(msg.encode())
                print(tcp_client_socket.recv(1025).decode())
                if msg[0:3] == 'bye':
                    break
                msg = tcp_client_socket.recv(4096).decode()
                print(f'Server: {msg}')
                tcp_client_socket.send(
                    bytes("sucesfuly reciver your messages\n Typing....", 'utf-8'))

finally:
    tcp_client_socket.close()
