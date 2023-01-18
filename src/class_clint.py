import socket

class Client:

    def __init__(self, ip, port):
        self.serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.ip = ip
        self.port = port

    def connect(self):
        self.serverSocket.connect((self.ip, self.port))

    def getMessage(self):
        return self.serverSocket.recv(1024).decode('ascii')

    def modifyMessage(self):
        return message.upper()

    def sendMessage(self, upperCaseMessage, server):
        (server, addr) = self.serverSocket.accept()
        self.serverSocket.send(upperCaseMessage.encode('ascii'))

    def closeConnection(self):
        self.serverSocket.close()


if __name__ == '__main__':
    myClient = Client('127.0.0.1', 5555)
    myClient.connect()
    message = myClient.getMessage()
    upperCaseMessage = myClient.modifyMessage()
    myClient.sendMessage(upperCaseMessage)
    myClient.closeConnection()
