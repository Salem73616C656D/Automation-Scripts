#! /bin/bash
# Script Name:      System Spec. List
# Author:           marburgja
# Last Rev:         20210907
# Purpose:          lists system spec. information

# Libraries
import subprocess

# Main

print("Hostname")
host=subprocess.run(["hostname"])

print("Username")
user=subprocess.run(["whoami"])

print("CPU")
cpu=subprocess.run(["lshw", "-c", "processor"])

print ("Display Adapter")
dispad=subprocess.run(["lshw", "-c", "display"])

print ("Network Adapter")
netad=subprocess.run(["lshw", "-c", "network"])

# End