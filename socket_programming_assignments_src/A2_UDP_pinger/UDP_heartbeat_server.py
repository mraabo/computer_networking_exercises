# We will need the following module to generate randomized lost packets
import random
import time
from socket import *

# Create a UDP socket 
# Notice the use of SOCK_DGRAM for UDP packets
server_socket = socket(AF_INET, SOCK_DGRAM)
# Assign IP address and port number to socket
server_socket.bind(('', 12000))

expected_seq_num = 0

print("Ready to serve...")   
while True:
    try:
        # Parse packet information.
        message, address = server_socket.recvfrom(1024)
        server_socket.settimeout(1)
        received_time = time.time()

        sent_time = float(message.decode().split()[2])
        seq_number = message.decode().split()[1]
        
        # Organize packet information.
        if seq_number != expected_seq_num:
            print("Packet" + str(expected_seq_num) + " was lost.")

            expected_seq_num += 1
        print("Packet" + str(expected_seq_num) + " was received in " + str(received_time - sent_time) + " seconds.")
        expected_seq_num += 1
    except timeout:
        print("Server timed out. No packet received for 1 second. Assuming client application has stopped.")
        break







