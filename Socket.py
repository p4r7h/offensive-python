import socket 

tcpsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
# socket.AF_INET -> address family 
# socket,SOCK_STREAM -> kind of socket its tcp

tcpsocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# this will allow to reuse ip address when server crash or exit without any reson

tcpsocket.bind("0.0.0.0", 8000)
# its and bind call thats tacks two argumets ip and port

tcpsocket.listen(2)
# listen tackes one argumets thats number of user can connect in our case its 2

(client, (ip, port)) = tcpsocket.accept()
# this contain ip and port of user thats connect with client and create new socket for diffrent diffrent users and its waiting for client

client.send("Welcome to the World of Network Security")
# client.send -> send a welcome msg to the user

data = client.recv(2048)
# this recv data from the client of buufer 2048 and assign that in to datavariable

client.close()
# close client connection

tcpsocket.close()
# close the server 
