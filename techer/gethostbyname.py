#
# gethostbyname.py
#
import sys, socket, select

# host= "https://shikoku-u.manaba.jp/"


if len(sys.argv) == 2:
    host = sys.argv[1]
else:
    print('Usage: python3 gethostname.py <hostname> ')
    exit(0)
    
    
ipaddr = (socket.gethostbyname(host))
print(ipaddr)
