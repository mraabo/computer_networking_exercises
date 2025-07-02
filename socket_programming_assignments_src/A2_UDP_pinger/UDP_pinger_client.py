import time
import pandas as pd
from socket import *

server_name = "127.0.0.1"

server_port = 12000
client_socket = socket(AF_INET, SOCK_DGRAM)
client_socket.settimeout(1)

RTTs = {}
sequence_number = 0

for i in range(10):
    sequence_number += 1
    initial_time = time.time()
    message = f'Ping {sequence_number} {initial_time}\r\n\r\n'

    client_socket.sendto(message.encode(), (server_name, server_port))

    try:
        received_message = client_socket.recv(2048)
        end_time = time.time()
        print("From Server:", received_message.decode())
        RTTs["Packet: " + str(sequence_number)] = str(end_time - initial_time)
    except timeout:
        RTTs["Packet: " + str(sequence_number)] = "lost"

df = pd.DataFrame(RTTs.items(), columns=['Packet', 'RTT'])
print(df)
client_socket.close()