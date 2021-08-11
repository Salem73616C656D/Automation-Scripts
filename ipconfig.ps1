# Script Name:      IP Config Logger
# Author:           marburgja
# Last Rev:         20210810
# Purpose:          Export IPConfig /All Results Into A .TXT

# Variables
$path="C:\users\joshm\desktop\network_report.txt"

# Functions
function uneccessaryroute {
    ipconfig /all | out-file -filepath $path
    select-string -path $path -pattern ipv4 -simplematch | select-object -first 1 | write-host
    remove-item $path
}

# Main
uneccessaryroute