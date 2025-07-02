import time
import pandas as pd
from socket import *

server_name = "127.0.0.1"

server_port = 12000
client_socket = socket(AF_INET, SOCK_DGRAM)

sequence_number = 0

for i in range(10):
    sequence_number += 1
    initial_time = time.time()
    message = f'Ping {sequence_number} {initial_time}\r\n\r\n'
    client_socket.sendto(message.encode(), (server_name, server_port))
client_socket.close()