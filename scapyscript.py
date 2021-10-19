#! /usr/bin/env python3
# Script Name:      scapy
# Author:           marburgja
# Last Rev:         20211018
# Purpose:          TCP Port Range Scanner
# Sources:          https://github.com/ewhd/ops401d2/blob/master/challenge411-scapy-security-tool1.py
#                   https://thepacketgeek.com/scapy/building-network-tools/part-10/

# Libraries
from scapy.layers.inet import IP, ICMP, TCP, sr, sr1
import random
# importing "from scapy.all import *" didn't work. I had to import from the layers.inet folder to get them to populate
# import issue causing script to spit out "No protocol specified"



# Variables
# IP,ICMP,TCP,sr,sr1
ip=input("Enter IP Address To Scan:") or "44.33.32.156"

ports=[22, 80, 389, 443, 3389]


# Functions
def scanner():
    # Send SYN with random Source Port for each Destination Port
    for port in ports:
        src_port=random.randint(1025,65534)
        #src_port=1025
        resp=sr1(
            IP(dst=ip)/TCP(sport=src_port,dport=port,flags="S"),
            timeout=1,
            verbose=0)
        #print(resp)
            
        if resp is None:
            print(f"{ip}:{port} is filtered (silently dropped).")
        
        elif(resp.haslayer(TCP)):
            if(resp.getlayer(TCP).flags == 0x12):
                # Send a gratuitous RST to close the connection
                send_rst=sr(
                    IP(dst=ip)/TCP(sport=src_port,dport=port,flags='R'),
                    timeout=1,
                    verbose=0
                )
                send_rst
                print(f"{ip}:{port} is open.")
            
            elif (resp.getlayer(TCP).flags == 0x14):
                print(f"{ip}:{port} is closed.")

        elif(resp.haslayer(ICMP)):
            if(
                int(resp.getlayer(ICMP).type) == 3 and
                int(resp.getlayer(ICMP).code) in [1,2,3,9,10,13]
            ):
                print(f"{ip}:{port} is filtered (silently dropped).")


# Main
scanner()

# End
