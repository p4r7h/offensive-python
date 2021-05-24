#!/usr/bin/python

import socket
import thread
import sys
import random

def EchoClientHandler(clientSocket, addr) :
	while 1:
		client_data  = clientSocket.recv(2048)
		if client_data :
                        print "client {} : {}".format(addr , client_data)
			clientSocket.send(client_data)
		else :
			clientSocket.close()
			return



echoServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

echoServer.bind(("0.0.0.0", int(sys.argv[1])))
echoServer.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
echoServer.listen(10)

while 1:
	cSock, addr = echoServer.accept()
	# id = random.randint(501,999)
	# print "Client Connect to id : "
	# start a new thread to service 
	thread.start_new_thread(EchoClientHandler, (cSock, addr))
