import ssl
import os # to get current directory
from socket import *

message_body = "\r\n I love computer networks!"
message_end = "\r\n.\r\n"

# Choose a mail server (e.g. Google mail server) and call it mailserver
mailserver = "smtp.gmail.com"
server_port = 587

# Create socket called clientSocket and establish a TCP connection with mailserver
client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect((mailserver, server_port))

recv = client_socket.recv(1024).decode()
print(recv)
if recv[:3] != '220':
    print('220 reply not received from server.')

# Send HELO command and print server response.
helo_cmd = 'HELO crepes.fr\r\n'
client_socket.send(helo_cmd.encode())
recv1 = client_socket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')

# Send STARTTLS command to see if TLS is available,
# also print server response and wrap client socket in SSL.
start_tls_cmd = "STARTTLS\r\n"
client_socket.send(start_tls_cmd.encode())
recv2 = client_socket.recv(1024).decode()
print(recv2)
if recv2[:3] != "220":
    print("220 reply not received from server.")
client_socket = ssl.wrap_socket(client_socket)

# Send 2nd hello after establishing TLS connection,
# since server is supposed to forget previous activity.
client_socket.send(helo_cmd.encode())
recv3 = client_socket.recv(1024).decode()
print(recv3)
if recv3[:3] != "250":
    print('250 reply not received from server.')

# Send AUTH command and print server response.
filename = "auth.txt"
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
f = open(os.path.join(__location__, filename[1:]))
auth_str = f.read()

auth_cmd = f"AUTH {auth_str}"
client_socket.send(auth_cmd.encode())
recv4 = client_socket.recv(1024).decode()
print(recv4)
if recv4 != "530":
    print("530 reply not received from server.")

# Send MAIL FROM command and print server response.
mail_from_cmd = "MAIL FROM: <alice@crepes.fr>"
client_socket.send(mail_from_cmd.encode())
recv5 = client_socket.recv(1024).decode()
print(recv5)
if recv5[:3] != "250":
    print('250 reply not received from server.')

# Send RCPT TO command and print server response. 
rcpt_to_cmd = "RCPT TO: <magnusraabo@gmail.com>"
client_socket.send(rcpt_to_cmd.encode())
recv6 = client_socket.recv(1024).decode()
print(recv6)
if recv6[:3] != "250":
    print('250 reply not received from server.')


# Send DATA command and print server response. 
data_to_cmd = "DATA"
client_socket.send(data_to_cmd.encode())
recv7 = client_socket.recv(1024).decode()
print(recv7)
if recv7[:3] != "354":
    print('354 reply not received from server.')


# Send message data.
client_socket.send(message_body.encode())
# Message ends with a single period.
client_socket.send(message_end.encode())
recv8 = client_socket.recv(1024).decode()
print(recv8)
if recv8[:3] != "250":
    print('250 reply not received from server.')


# Send QUIT command and get server response.
quit_cmd = "QUIT"
client_socket.send(quit_cmd.encode())
recv9 = client_socket.recv(1024).decode()
print(recv9)
if recv9[:3] != "221":
    print('221 reply not received from server.')
client_socket.close()
