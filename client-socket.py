#!/usr/bin/python

import socket
import sys

tcpsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

tcpsocket.connect((sys.argv[1], 8000))

while 1 :
	userinput = raw_input("pleas enter a string :")
	tcpsocket.send(userinput)
	print tcp.socket.recv(2048)

tcpsocket.close()
