from socket import *
my_ip = gethostbyname(gethostname())
serverName = my_ip
serverPort = 14000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
sentence = input("Input lowercase sentence:")
clientSocket.send(sentence.encode())
modifiedSentence = clientSocket.recv(1024)
print("From Server: ", modifiedSentence.decode()) 
clientSocket.close()