#
# tcp_server.py
#
import sys, socket, select

import sqlite3
conn = sqlite3 . connect('user.db')
cursor = conn.cursor()

conn.execute('''CREATE TABLE IF NOT EXISTS  users
         (username  TEXT    NOT NULL);''')


# ip = '172.30.56.168'
ip = "127.0.0.1"
port = 8880

tcp_user = ["yabindra"]




tcp_listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_listen_socket.bind((ip, port))
tcp_listen_socket.listen(5)
print(
    f"Server is runnig in {ip} {port} \n waiting for connection ...")

while True:
    tcp_accepted_socket, peeraddr = tcp_listen_socket.accept()
    
    

    username = tcp_accepted_socket.recv(1024).decode()
    query = 'SELECT * FROM users WHERE username = ?'
    cursor.execute(query, (username,))
    result = cursor.fetchone()
    
    if username in result:
        tcp_accepted_socket.send(bytes("Welocme to chat group", 'utf-8'))
        print(username, " is connection with", peeraddr)
        while True:
            msg = tcp_accepted_socket.recv(4096).decode()
            print(f'{username }: {msg}')
            tcp_accepted_socket.send(
                bytes("sucesfuly reciver your messages\n Typing....", 'utf-8'))
            if msg[0:3] == 'bye':
                break
            msg = input('message : ')
            tcp_accepted_socket.send(msg.encode())
            recive = tcp_accepted_socket.recv(4096).decode()
            print(recive)
    
    # elif username not in result:
    else:
        while True:
            tcp_accepted_socket.send(bytes("username is invalid \n if you want to add your name in group enter y or Y", 'utf-8'))
            newuser = tcp_accepted_socket.recv(1024).decode('utf-8')
            tcp_user.append(newuser)
        
            query = 'INSERT INTO users (username) VALUES (?)'
            cursor.execute(query, (newuser,))
            conn.commit()
  
       
        
        
            tcp_accepted_socket.send(bytes(" is added sucessfuly", 'utf-8'))
            print(tcp_user)
            print(username, " is connection with", peeraddr)
    
        
    # while True:
            msg = tcp_accepted_socket.recv(4096).decode('utf-8')
            print(f'{username }: {msg}')
            tcp_accepted_socket.send(
            bytes("sucesfuly reciver your messages\n Typing....", 'utf-8'))
            if msg[0:3] == 'bye':
                break
            msg = input('message : ') 
            tcp_accepted_socket.send(msg.encode())
            recive = tcp_accepted_socket.recv(4096).decode()
            print(recive)
     
     

    tcp_accepted_socket.close()
    tcp_listen_socket.close()
