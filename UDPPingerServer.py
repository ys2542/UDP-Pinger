# Name: Shen, Yulin
# NetID: ys2542

# UDPPingerServer.py
# The code is completely taken from companion website for the textbook in www.pearsonhighered.com/cs-resources
# I add an option in terminal command line to manually set server port number
# I add two print methods to see messages and cases of packet lost

# We will need the following module to generate randomized lost packets
import sys
import random
from socket import *

# Check terminal command and print the right format if wrong
if (len(sys.argv) != 2):
    print('Format: python UDPPingerServer.py <Server_Port_Number>')
    sys.exit()

# Create a UDP socket
# Notice the use of SOCK_DGRAM for UDP packets
serverSocket = socket(AF_INET, SOCK_DGRAM)

# Assign IP address and port number to socket
port = int(sys.argv[1])
serverSocket.bind(('', port))

while True:
	# Generate random number in the range of 0 to 10
	rand = random.randint(0, 10)
	# Receive the client packet along with the address it is coming from
	message, address = serverSocket.recvfrom(1024)
	# Capitalize the message from the client
	message = message.upper()
	# Print message for demo
	print(message)
	# If rand is less is than 4, we consider the packet lost and do not respond
	if rand < 4:
		# Print message for packet lost
		print('Packet lost')
		continue
	# Otherwise, the server responds
	serverSocket.sendto(message, address)
