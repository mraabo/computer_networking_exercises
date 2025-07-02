from socket import *
import time 


server_name = "127.0.0.1"

server_port = 12000
client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect((server_name, server_port))
message = 'GET /hello_world.html HTTP/1.1\r\n\r\n'

client_socket.send(message.encode())

time.sleep(1) # wait for 1 second to ensure packet is received before closing socket.

received_message = client_socket.recv(2048)
print("From Server:", received_message.decode())
client_socket.close()