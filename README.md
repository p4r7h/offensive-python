# offensive-python

## Signals

- Allows handling of asynchronous events
- SIGKILL is what gets sent when you use `kill -9`
- programing with signals is easy


## Socket Programming

- TCp and UDP sockets
    - Regular Servers and clients
- Raw Sockets
    - Sniffing and Injection
    
    
## WEB Server

How does a Web Application Server Work?

- listen on port 80 / 443
- wait for client requests (GET, POST, HEAD ...)
- process Request
    - Serve Files
    - execute CGI scripts
    
   
# Packet Sniffing With Raw Socket

- Raw Sockets provide a way to bypass the whole network stack traversal of a packet and deliver it directly to an application

## PF_PCAKET

- it is softwhere interface to send / receive packets at layer 2 of the OSI i.e device driver
- all packets received will be complete with all headers and data
- all packets sent will be transmitted without modification by the kernel to the medium
- supports filering using berkley packet filter

### Creating RAW Sockets

- use the socket module
- read packets
- interpret and analyze them
- can send out responses as well


## Packet Injection with Raw Sockets

- ability to inject raw packets into the network
- powerful as we can stimulate responses from the Network
- packet construction not scalable with raw socket

# Packet Sniffing with scapy

- raw sockets are painful to use and not too portable acress OSs
- Use of 3rd Part libs :
    - pylibpcap
    - pycapy
    - pypcap
    - impacket
    - scapy
-scapy
- interactive mode or use as library
- can be used for packet sniffing and forging
- tons of protocols already implemented
- Allowd to build "reactive" tools

# Attacking Web Pages

### Fetching Web pages

- most basic of functionality to fetch data
- urllib, urllib2
- allows for arguments encoding




