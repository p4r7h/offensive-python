#!/usr/bin/python

import scoket
import struct
import binascii

rawsocket = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.htons(0x0800))
# PF_PACKET this specify the packet interace , SOCK_RAW specify the raw socket and 
# the 3 argument specify that in which protocol we are intrested in 0x0800 specify that we are intrested in internet protocol packet

pkt = rawsocket.recvfrom(2048)
# its recive a packets and stored in pkt variouble that contains lots of info in form of tuple

ether = pkt[0][0:14]
# its take out only packet from the pkt (14 bytes) 
# first 6 bytes is destination mac address 
# next 6 bytes is sorce mac address and last 2 bytes is ether type

eth_hdr = struct.unpack("!6s6s2s",ether)
# !6s6s2s from 6s taking frist 6 bytes together again 6 more and last one 2s takes last 2 bytes that was the actual value of the ether type

binascii.hexlify(eth_hdr[0])
# its print out values in hex 
# print destination mac address inn hex
binascii.hexlify(eth_hdr[1])
# print source mac address in hex
binascii.hexlify(eth_hdr[2])
# print ether type for ip 

ipheader = pkt[0][14:34]
# its takes next 20 bytes 

ip_hdr = struck.unpack("!12s4s4s", ipheader)
# its uncapsulate ipheader 
# in this case first 12 bytes cosist version , IHL and type of service  , IDENTIfication, TIME TO LIVE , PROTOCOL
#  and the 4 bytes contain source ip address and last 4 bytes consist destination ip address 


print " Source IP : " + socket.inet_ntoa(ip_hdr[1])
# this print out source ip and we are using function inet_ntoa this is network to ip
print " Source IP : " + socket.inet_ntoa(ip_hdr[2])
