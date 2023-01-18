#
# chatd.py
#
import sys, socket, select

class session_end(Exception):
    pass

tcp_listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_listen_socket.bind(('0.0.0.0', 10001))
tcp_listen_socket.listen(5)
print("Server is running ..\n waiting for connection ")

while True:
    tcp_accepted_socket, peeraddr = tcp_listen_socket.accept()
    print(f"User is connection on \n{peeraddr}")
    ipaddr, port = peeraddr
   

    try:
        while True:
            ready, w, x = select.select([sys.stdin, tcp_accepted_socket], [], [])

            for io in ready:
                if io == tcp_accepted_socket:
                    # 相手からのメッセージを受け取って表示する
                    msg = tcp_accepted_socket.recv(4096).decode()
                    if msg != None:
                        print('%s:%d> ' % (ipaddr, port) + msg)
                    if msg == None or msg == '' or msg == 'bye':
                        raise session_end # session end

                if io == sys.stdin:
                    # こちらのメッセージを相手に送る
                    msg = input().rstrip(' \n')
                    tcp_accepted_socket.send(msg.encode())
                    if msg == None or msg == '' or msg == 'bye':
                        raise session_end # session end

    except session_end:
        pass

    finally:
        print('session end...')
        tcp_accepted_socket.close()

        tcp_listen_socket.close()
