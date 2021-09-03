#! /bin/bash/
# Script Name:      logclear
# Author:           marburgja
# Last Rev:         20210903
# Purpose:          clear syslog and wtmp logs
# Conditions:       **Run Sudo**
# Variables

dir=/var/log/

# Functions
# Change > *** to whatever log file you want to clear
clearlogs(){
    cat /dev/null > syslog
    cat /dev/null > wtmp
    cat /dev/null > auth.log
    cat /dev/null > kern.log
    cat /dev/null > pureftp.log
    cat /dev/null > faillog
    cat /dev/null > daemon.log
    cat /dev/null > kern.log
}

# Main

# Change to /var/log directory
cd $dir

# Print syslog and wtmp to terminal
cat syslog
cat wtmp

# Clear chosen logs
clearlogs
echo "Clear Successful"

# Print syslog and wtmp to terminal again
cat syslog
cat wtmp

# End




# syslog: Shows general messages and info regarding the system. Basically a data log of all activity 
# throughout the global system. Know that everything that happens on Redhat-based systems, like CentOS or Rhel, will go in messages.
# Whereas for Ubuntu and other Debian systems, they go in Syslog.

# auth.log: keeps authentication logs (success/failure) (RH, CentrOS goes to /var/log/secure)

# kern.log: logs from kernel as well as warning info

# wtmp: login/logout records

# pureftp.log: monitors for FTP connections using pureftp process

# daemon.log: keeps track of background services

# faillog: records failed login attempts