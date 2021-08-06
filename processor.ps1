# Script Name:      Process Printer
# Author:           marburgja
# Last Rev:         20210806
# Purpose:          Print, Create, and Kill Various Processes

# Main

# prints/sorts all running processes by CPU usage high>low
get-process | sort cpu -descending

# prints/sorts all running processes by PID number high>low
get-process | sort id -descending

# prints/sorts all running processes by Working Set high>low
get-process | sort ws -descending

# open internet explorer to *website*
[system.diagnostics.process]::start("iexplore","https://owasp.org/www-project-top-ten/")

# change to "chrome" "msedge" "firefox" for different browsers
start-job -scriptblock {10 | foreach-object {[system.diagnostics.process]::start("iexplore","https://owasp.org/www-project-top-ten/")}}

# open multiple internet explorer windows to *website*
$variable=10
for ($x=0;$x -lt $variable;$x++)
{
    [system.diagnostics.process]::start("iexplore","https://owasp.org/www-project-top-ten/")
}

# kill a process by name
Stop-Process -name iexplore

# kill a process by PID
Stop-Process -id 3680

# End