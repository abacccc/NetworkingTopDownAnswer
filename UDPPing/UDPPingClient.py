from socket import *
import time

target = 'localhost'
port = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.settimeout(1)
print('Ping: %s' % (target))
for i in range(10):
    sendTime = time.time()
    try:
        clientSocket.sendto('ping'.encode(), (target, port))
        msg, serverAdd = clientSocket.recvfrom(1024)
        rtt = time.time() - sendTime
        print('Sequence number: %d, time: %.7fs' % (i, rtt))
    except Exception as e:
        print('Sequence number: %d, Timeout' % (i))
clientSocket.close()
