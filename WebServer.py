# Name: Shen, Yulin
# NetID: ys2542

# WebServer.py
# The code is based on the skeleton code taken from companion website for the textbook in www.pearsonhighered.com/cs-resources

# We will need the following module to make a web server
import sys
from socket import *

# Check terminal command and print the right format if wrong
if (len(sys.argv) != 2):
    print('Format: python WebServer.py <Server_Port_Number>')
    sys.exit()

# Create a UDP socket
# Notice the use of SOCK_DGRAM for UDP packets
serverSocket = socket(AF_INET, SOCK_STREAM)

# Assign IP address and port number to socket
serverSocket.bind(('', int(sys.argv[1]))) 

# Wait for at most one request at a time
serverSocket.listen(1) 

while True:
    # Establish a new connection
    connectionSocket, addr = serverSocket.accept() 

    try:
        # Receive the message from the client
        message = connectionSocket.recv(1024).decode()
        # Extract the path from the message
        filename = message.split()[1]
        # Read the path
        f = open(filename[1:], 'r')
        outputdata = f.read()

        # Send the response message
        connectionSocket.send('HTTP/1.1 200 OK\r\n\r\n'.encode())
        # Send the content
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send('\r\n'.encode())

        # Close the client connection
        connectionSocket.close()

    except IOError:
        # send the response menssage
        connectionSocket.send('HTTP/1.1 404 Not Found\r\n\r\n'.encode())
        connectionSocket.send('<html><head></head><body><h1>404 Not Found</h1></body></html>\r\n'.encode())
        
        # Close the client connection
        connectionSocket.close()

# Close the UDP socket
serverSocket.close()
