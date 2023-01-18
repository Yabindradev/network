#
# tcp_client.py
#
import sys, socket, select


try:
    tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_client_socket.connect(('127.0.0.1', 8880))
    
  
    name = input("Username: ")
    tcp_client_socket.send(bytes(name, 'utf-8'))
  

    
except Exception:
    print('Server is not ready to connection')
else:
    while True:
        error = tcp_client_socket.recv(1024).decode('utf-8')
    
        if error == "username is invalid \n if you want to add your name in group enter y or Y":
            print(error)
            newu = input()
            if newu == "y" or newu == "Y":
                newuser = input("Enter username: ")
                tcp_client_socket.send(bytes(newuser, 'utf-8'))
                added_user = tcp_client_socket.recv(1024).decode('utf-8')
                print(newuser, added_user)
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
                
            else:
                print("Can not access in group \n --------------------")
                break
        else:
            
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
            
finally:
    tcp_client_socket.close()



