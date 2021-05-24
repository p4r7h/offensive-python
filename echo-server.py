import socket

tcpsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpsocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

tcpsocket.bind(('0.0.0.0', 8000))
tcpsocket.listen(1)

hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)

print "Waiting for Clients to connect AT local ip : ",local_ip

(client, (ip, port)) = tcpsocket.accept()

print "Connect To ",ip,port

data = "Dummy"

while len(data) :
    data = client.recv(2048)
    print "client : ",data
    client.send(data)

client.close()
tcpsocket.close()
