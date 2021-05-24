# sudo scapy

pkts = sniff(iface="eth1", count=3)
# its going to sniff packets sniff funcation tackes 2 argument first one contain network info and secound argument contains number of packets 

pkts
# gives you basic statastick of the packts 

pkts[0]
# its give you a indivisual packts 

pkts[0].show
# its give you beutiful view and suparets all the filed

wrpcap("filname.pcap", pkts)
# write packets to a pcap file 

read_pkts = rdpcap("filename.pcap")
# read packets from the file
