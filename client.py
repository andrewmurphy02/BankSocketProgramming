''' client.py
usage: python client.py HOSTNAMEorIP PORT
takes input from user, sends to server, and prints answer
Modified by Andrew Murphy 010936341
'''

import sys

# Import socket library
from socket import *
def menu():
    print("Welcome to the ATM")
    print("Press 1 for Deposit.")
    print("Press 2 for Withdrawal")
    print("Press 3 for Account Balance")
    print("Press 4 to Quit")
# Set hostname or IP address from command line or default to localhost
# Set port number by converting argument string to integer or use default
# Use defaults
if sys.argv.__len__() != 3:
    serverName = 'localhost'
    serverPort = 5556
# Get from command line
else:
    serverName = sys.argv[1]
    serverPort = int(sys.argv[2])

# Choose SOCK_DGRAM, which is UDP
clientSocket = socket(AF_INET, SOCK_DGRAM)


menu() # Calling menu method to display menu to the user
while 1:
    print("What would you like to do: ")
    userchoice = input()
    if userchoice=="1":
        # deposit amount
        total = input("Enter amount to deposit: ")
        messageBytes = userchoice.encode('utf-8')
        messageBytes2 = total.encode('utf-8')
        clientSocket.sendto(messageBytes,(serverName, serverPort))
        clientSocket.sendto(messageBytes2,(serverName, serverPort))
        modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
        modifiedMessageString = modifiedMessage.decode('utf-8')
        print("Your account balance is: $"+modifiedMessageString)
    
        #clientSocket.close()
    elif userchoice=="2":
        # withdraw amount
        total = input("Enter amount to withdraw: ")
        messageBytes = userchoice.encode('utf-8')
        messageBytes2 = total.encode('utf-8')
        clientSocket.sendto(messageBytes,(serverName, serverPort))
        clientSocket.sendto(messageBytes2,(serverName, serverPort))
        modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
        modifiedMessageString = modifiedMessage.decode('utf-8')
        print("Your account balance is: $"+modifiedMessageString)
        #clientSocket.close()
    elif userchoice=="3":
        messageBytes = userchoice.encode('utf-8')
        messageBytes2 = "".encode('utf-8')
        clientSocket.sendto(messageBytes,(serverName, serverPort))
        clientSocket.sendto(messageBytes2,(serverName, serverPort))
        modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
        modifiedMessageString = modifiedMessage.decode('utf-8')
        print("Your account balance is: $"+modifiedMessageString)
        #clientSocket.close()
    elif userchoice=="4":
        messageBytes = userchoice.encode('utf-8')
        messageBytes2 = "".encode('utf-8')
        clientSocket.sendto(messageBytes,(serverName, serverPort))
        clientSocket.sendto(messageBytes2,(serverName, serverPort))
        modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
        modifiedMessageString = modifiedMessage.decode('utf-8')
        print("Your account balance is: $"+modifiedMessageString+" quiting server")
        clientSocket.close()
        break
        