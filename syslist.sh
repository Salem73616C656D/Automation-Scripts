#! /bin/bash
# Script Name:      System Spec. List
# Author:           marburgja
# Last Rev:         20210803
# Purpose:          lists system spec. information

# Variables
host=$(hostname)

# Functions
compname(){
    echo "$host"
}
cpu(){
    echo "CPU"
    sudo lshw -class processor | grep -E 'product|vendor|physical id|bus info|width'
}

memory(){
    echo "RAM"
    sudo lshw -class memory | awk 'NR==35,NR==36'
    sudo lshw -class memory | awk 'NR==38'
}

display(){
    echo "Display Adapter"
    sudo lshw -class display | grep -E 'description|product|vendor|physical id|bus info|width|clock|capabilities|configuration|resources'
}

network(){
    echo "Network Adapter"
    sudo lshw -class network | grep -E 'description|product|vendor|physical id|bus info|logical name|version|serial|size|capacity|width|clock|capabilities|configuration|resources'
}



# Main
echo "Retrieving System Information..."
sleep 3
compname
cpu
memory
display
network

# End
