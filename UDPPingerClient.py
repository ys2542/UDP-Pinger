# Name: Shen, Yulin
# NetID: ys2542

# UDPPingerClient.py
# The code is imitated from UDPPingerServer.py

# We will need the following module to record Round Trip Time (RTT)
import sys
from socket import *
from time import time, ctime

# Check terminal command and print the right format if wrong
if (len(sys.argv) != 2):
    print('Format: python UDPPingerClient.py <Server_Port_Number>')
    sys.exit()

# Create a UDP socket
# Notice the use of SOCK_DGRAM for UDP packets
clientSocket = socket(AF_INET, SOCK_DGRAM)
# Assume client waits up to one second for a reply from the server
clientSocket.settimeout(1)

# Assign IP address and port number to socket
port = int(sys.argv[1])
serverSocket = ('', port)

# Send 10 ping messages to the target server over UDP
for i in range(10):
    # Record the start time
    sendTime = time()
    # Create a message with the current time
    message = 'Ping message ' + str(i+1) + ' ' + ctime(sendTime)[11:19]
    # Send the message to the server
    clientSocket.sendto(message.encode(), serverSocket)

    # Successfully receive pong messages in one second
    try:
        # Wait pong messages from the server
        pong, serverAddress = clientSocket.recvfrom(1024)
        # Record the finish time
        receiveTime = time()
        # Calculate RTT
        rtt = receiveTime - sendTime
        # Print the pong message and Round Trip Time
        print('Pong message:', pong.decode())
        print('Round Trip Time:', rtt,'\n')

    # Not receive pong messages due to request time out
    except timeout:
        # Print the time out message and the ping message number
        print("Ping message %i request time out\n" %(i+1))

# Close the UDP socket
clientSocket.close()
