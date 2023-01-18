#
# chat.py
#
import sys, socket, select

class session_end(Exception):
    pass

# ipaddr = '127.0.0.1'
ipaddr = '172.30.56.168'

port = 10000

try:
    tcp_client_socket = socket.create_connection((ipaddr, port))

except Exception:
    print('tcp socket connect error')

else:
    try:
        while True:
            ready, w, x = select.select([sys.stdin, tcp_client_socket], [], [])

            for io in ready:
                if io == sys.stdin:
                    # こちらのメッセージを相手に送る
                    msg = input().rstrip(' \n')
                    tcp_client_socket.send(msg.encode())
                    if msg == None or msg == '' or msg == 'bye':
                        raise session_end

                if io == tcp_client_socket:
                    # 相手からのメッセージを受け取って表示する
                    msg = tcp_client_socket.recv(4096).decode()
                    if msg != None:
                        print('%s:%d> ' % (ipaddr, port) + msg)
                    if msg == None or msg == '' or msg == 'bye':
                        raise session_end

    except session_end:
        pass

    finally:
        print('session end...')
        tcp_client_socket.close()

finally:
    pass
