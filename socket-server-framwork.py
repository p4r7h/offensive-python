#!/usr/bin/python

import SocketServer


serveraddr = ("ip", port)
# mention server address 

server = SocketServer.TCPServer(serveraddr, echo)
# this invoke tcpserver and pass two arguments that contain server address in first arg and secound arg contains class that handle clients that connect with server

server.server_forever()
# its run forever and handle clients as much as possible

class echo(SocketServer.BaseRequestHandler) :
	def handle(self) :
	# to do
