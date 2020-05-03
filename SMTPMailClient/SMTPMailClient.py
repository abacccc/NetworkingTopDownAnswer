from socket import *
msg = '\r\n I love computer networks!'
endmsg = '\r\n.\r\n'
# Choose a mail server (e.g. Google mail server) and call it mailserver
mailServer = '*****************'
port = 25
# Create socket called clientSocket and establish a TCP connection with mailserver
#Fill in start
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((mailServer, port))
#Fill in end
recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '220':
    print('220 reply not received from server.')
# Send HELO command and print server response.
heloCommand = 'HELO Alice\r\n'
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')

# Send MAIL FROM command and print server response.
# Fill in start
mailFromCommand = 'MAIL FROM: <***********>\r\n'
clientSocket.send(mailFromCommand.encode())
recvMailFrom = clientSocket.recv(1024).decode();
print(recvMailFrom)
if recvMailFrom[:3] != '250':
    print('250 reply not received from server.')
# Fill in end
# Send RCPT TO command and print server response.
# Fill in start
rcptToCommand = 'RCPT TO: <***************>\r\n'
clientSocket.send(rcptToCommand.encode())
recvRcptTo = clientSocket.recv(1024).decode();
print(recvRcptTo)

# Fill in end
# Send DATA command and print server response.
# Fill in start
# Fill in end
# Send message data.
# Fill in start
# Fill in end
# Message ends with a single period.
# Fill in start
# Fill in end
# Send QUIT command and get server response.
# Fill in start
# Fill in end
