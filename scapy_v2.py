#! /usr/bin/env python3
# Script Name:      scapy
# Author:           marburgja
# Last Rev:         20211018
# Purpose:          TCP Port Range Scanner
# Sources:          https://github.com/ewhd/ops401d2/blob/master/challenge411-scapy-security-tool1.py
#                   https://thepacketgeek.com/scapy/building-network-tools/part-10/
#                   https://stackoverflow.com/questions/25980777/new-to-scapy-trying-to-understand-the-sr

# Libraries
from scapy.layers.inet import IP, ICMP, TCP, sr, sr1
import random
# importing "from scapy.all import *" didn't work. I had to import from the layers.inet folder to get them to populate
# import issue causing script to spit out "No protocol specified"
from ipaddress import IPv4Network

# Functions

def menu():
    print("1. Port Scanner")
    print("2. Ping Sweep")
    print("3. Exit")

def scanner():
    # Send SYN with random Source Port for each Destination Port
    ip=input("Enter IP Address To Scan:") or "44.33.32.156"
    ports=[22, 80, 389, 443, 3389]
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
                

def pinger():
    network=input("Enter CIDR Address To Scan( i.e. 10.10.0.0/24 ):")
    addresses=IPv4Network(network)
    live_count=0
    # Send ICMP requests and return results
    for host in addresses:
        if (host in (addresses.network_address, addresses.broadcast_address)):
            # Skip network and broadcast addresses
            continue

        # Assigning the ping response to variable "resp"
        resp=sr1(
            IP(dst=str(host))/ICMP(),
            timeout=1,
            verbose=0,
            # nofilter: put 1 to avoid use of bpf filters
            # retry:    if positive, how many times to resend unanswered packets
            #           if negative, how many times to retry when no more packets are answered
            # timeout:  how much time to wait after the last packet has been sent
            # verbose:  set verbosity level
            # multi:    whether to accept multiple answers for the same stimulus
            # filter:   provide a BPF filter
            # iface:    listen answers only on the given interface
        )

        if resp is None:
            print(f"{host} IS NOT RESPONDING.")
        elif(
            int(resp.getlayer(ICMP).type)==3 and
            int(resp.getlayer(ICMP).code) in [1,2,3,9,10,13]
        ):
            print(f"{host} IS BLOCKING ICMP.")
        else:
            print(f"{host} IS RESPONDING.")
            live_count += 1
    # Print total number of ONLINE hosts    
    print(f"{live_count}/{addresses.num_addresses} HOSTS ARE ONLINE.")


def main():
    # Ye Ol' LÖÖP
    while True:
        menu()
        choice = input("Please Select A Mode:")

        if choice=="1":
            scanner()

        elif choice=="2":
            pinger()
        
        elif choice=="3":
            break

        else:
            print("**Invalid Selection**")

# Main
main()

# End
