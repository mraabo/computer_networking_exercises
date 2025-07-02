#import socket module
from socket import *
import sys  # In order to terminate the program
import os # to get current directory

server_name = "127.0.0.1"
server_port = 12000

server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.bind(('', server_port))
server_socket.listen(1)
while True:
    # Establish the connection
    print('Ready to serve...')
    connection_socket, addr = server_socket.accept()
    try:
        message = connection_socket.recv(1024).decode()
        filename = message.split()[1]

        __location__ = os.path.realpath(
            os.path.join(os.getcwd(), os.path.dirname(__file__)))
        f = open(os.path.join(__location__, filename[1:]))
        output_data = f.read()
        
        # Send one HTTP header line into socket
        connection_socket.send('HTTP/1.1 200 OK\r\n\r\n'.encode()) 

        # Send the content of the requested file to the client
        for i in range(0, len(output_data)):
            connection_socket.send(output_data[i].encode())
        connection_socket.send("\r\n".encode())
        print("Packet sent")
        
        connection_socket.close()
    except IOError:
        # Send response message for file not found
        connection_socket.send("HTTP/1.1 404 Not Found\r\n\r\n".encode())
        # Close client socket
        connection_socket.close()

server_socket.close()
sys.exit() # Terminate the program after sending the corresponding data