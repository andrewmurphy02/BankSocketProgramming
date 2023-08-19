''' server.py
usage: python server.py PORT
Reads in text, computes mathematical computations, and returns
the value to the client
Modified by Andrew Murphy 010936341
'''

import sys

# Import socket library
from socket import *

# Set port number by converting argument string to integer
# If no arguments set a default port number
# Defaults
if sys.argv.__len__() != 2:
    serverPort = 5556
# Get port number from command line
else:
    serverPort = int(sys.argv[1])

# Choose SOCK_DGRAM, which is UDP
serverSocket = socket(AF_INET, SOCK_DGRAM)

# The SO_REUSEADDR flag tells the kernel to reuse a local socket
# in TIME_WAIT state, without waiting for its natural timeout to expire.
serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

# Start listening on specified port
serverSocket.bind(('', serverPort))

print("The server is ready to receive")
balance = 100
while 1:
    # Return data and address
    message, clientAddress = serverSocket.recvfrom(2048)
    message2, clientAddress = serverSocket.recvfrom(2048)
    message = message.decode('utf-8')
    message2 = message2.decode('utf-8')
    #balance = 100
   
    # deposit operation
    if message=="1":
        if message2.isdigit() == False:
            print("Not an integer!")
        elif int(message2) < 0:
            print("You cannot use negative numbers!")
        else:
            balance = balance + int(message2)
        
    elif message =="2":
        if message2.isdigit() == False:
            print("Not an intger!")
        # amount to be withdrawl greater than balance
        elif int(message2) > balance:
            print("You dont have enough balance to withdraw:")
        elif int(message2) < 0:
            print("You cannot use negative numbers!")
        else:
            # updated balance
            balance = balance - int(message2)
            
    # check balance
    elif message == '3':
        # displaying balance
        balance = balance
    
    # quiting from server
    elif message == '4':
        balance = balance
    # check for invalid input
    else:
        print("Invalid Input")
 
    modifiedMessage = balance
    modifiedMessageBytes = repr(modifiedMessage).encode('utf-8')

    # Send modified message back to client
    serverSocket.sendto(modifiedMessageBytes, clientAddress)

