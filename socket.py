#import socket module
from socket import *

serverSocket = socket(AP_INET, SOCK_STREAM)

#prepare a server socket

#Fill in start===================================

#Fill in end=====================================

while True:
	#Establish the connection
	print 'Ready to serve...'
	connectionSocket, addr = #Fill in start->		# <-Fill in end
	try: 
		message = #Fill in start		#<-Fill in end
		filename = message.split()[1]
		f = open(filename[1:])
		outputdata = #Fill in start->		#<-Fill in end

		#Send one HTTP line into socket

		#fill in start=======================
		#Fill in end=========================

		#Send the content of the requested file to the client
		for i in range(0, len(outputdata[i])
			connectionSocket.send(outputdata[i])
		connectionSocket.close()
	except IOError:
		#Send response message for file not found
		#Fill in start======================
		#Fill in end========================
		
		#Close client socket

		#FIll in start======================
		#Fill in end========================
		serverSocket.close()
