from socket import *

serverName = 'servername'
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print('Server ready to receive')

connectionSocket, addr = serverSocket.accept()
while True:
    sentence = connectionSocket.recv(1024).decode()
    print(sentence)
    connectionSocket.close()
