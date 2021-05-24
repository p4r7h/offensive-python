import socket 
import struct

rawsocket = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.htons(0x0800))

rawsocket.bind(("eth0", socket.htons(0x0800)))
# this will bind eth0 interface and we are using htons to specify the protocol we are intresred in 

packet = struct.pack("!6s6s2s",'\xaa\xaa\xaa\xaa\xaa\xaa','\xaa\xaa\xaa\xaa\xaa\xaa','\x08\x00')
# now we are actually pack the package that contains source and destination ip and ether type here we use 6s6s2s in that first 6 bytes contain destination address , another 6 bytes contains source address and the last 2 bytes contain a ether type that defult to ip

rawSocket.send(packet + "Hello There")
# its send and packets along with hello there msg
