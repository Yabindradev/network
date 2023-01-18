import sys, socket, select

ip = "127.0.0.1"
port = 8888
tcp_listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_listen_socket.bind((ip, port))
tcp_listen_socket.listen(5)

def send_mess():
    while True:
            msg = input('message:  ')
            tcp_client_socket.send(msg.encode())
            print(tcp_client_socket.recv(1025).decode())

            if msg == None or msg == '' or msg == 'bye':
                    break
            msg = tcp_client_socket.recv(4096).decode()
            print(f'Server: {msg}')
            tcp_client_socket.send(
                    bytes("sucesfuly reciver your messages\n Typing....", 'utf-8'))


send = send_mess()
