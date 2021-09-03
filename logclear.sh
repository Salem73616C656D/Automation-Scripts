#! /bin/bash/
# Script Name:      logclear
# Author:           marburgja
# Last Rev:         20210903
# Purpose:          clear syslog and wtmp logs

# Variables

dir=/var/log/

# Functions

clearlogs(){
    cat /dev/null > syslog
    cat /dev/null > wtmp
}

# Main

# Change to /var/log directory
cd $dir

# Print syslog and wtmp to terminal
cat syslog
cat wtmp

# Clear syslog and wtmp
clearlogs
echo "Clear Successful"

# Print syslog and wtmp to terminal again
cat syslog
cat wtmp

# End