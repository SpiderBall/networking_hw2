#import socket module
from socket import *

serverSocket = socket(AF_INET, SOCK_STREAM)

#prepare a server socket

#Fill in start===================================
serverPort = 12000
serverSocket.bid('',serverPort)
serverSocket.listen(1)
print 'The server is ready to receive'
#Fill in end=====================================

while True:
	#Establish the connection
	print 'Ready to serve...'
	connectionSocket, addr = serverSocket.accept()
	try: 
		message = connectionSocket.recv(1024)
		filename = message.split()[1]
		f = open(filename[1:])
		outputdata = f.read()#Fill in start->		#<-Fill in end

		#Send one HTTP line into socket
	 	connectionSocket.send(outputdata[0])

		#Send the content of the requested file to the client
		for i in range(0, len(outputdata[i])):
			connectionSocket.send(outputdata[i])
		connectionSocket.close()
	except IOError:
		#Send response message for file not found
		#Fill in start======================
		print "File not found"
		#Fill in end========================
		
		#Close client socket

		#FIll in start======================
		connectionSocket.close()
		#Fill in end========================
		serverSocket.close()
