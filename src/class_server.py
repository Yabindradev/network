import socket

class MySocket():
    
    def __init__(self, ip, port):
        self.serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.ip = ip
        self.port = port
        
    def bind(self):
        self.serverSocket.bind((self.ip, self.port))
        self.serverSocket.listen(5)
    
    def run(self):
        while True:
            
            print(f'Server is running in {self.ip} {self.port} \n Waiting for a connection')
            (clientSocket, addr) = self.serverSocket.accept()
            print('Got a connection from {}'.format(str(addr)))
            message = 'Congrats! You have connected'
            self.sendMessage(message, clientSocket)
            self.recieveMessage()
            clientSocket.close()

    def sendMessage(self, message, clientSocket):
        clientSocket.send(message.encode('ascii'))
        
        
    def recieveMessage(self):
        (clientSocket, addr) = self.serverSocket.accept()
        message = self.serverSocket.recv(1024).decode('ascii')
        print(message)
        
    def closeSocket(self):
        self.serverSocket.close()



myServer = MySocket('127.0.0.1', 8888)
myServer.bind()
myServer.run()
myServer.recieveMessage()
myServer.closeSocket()