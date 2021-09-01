# Script Name:      TimeStamp
# Author:           marburgja
# Last Rev:         20210831
# Purpose:          copies file to current directory

# Variables
date=$(date +"%T")

# Main
echo "Copying Syslog To Desktop $date..."
cp -r /var/log/syslog /home/marburgja/Desktop

echo "Switching To Desktop Directory $date..."
cd /home/marburgja/Desktop/

echo "Appending Date And Time To Filename $date..."
mv syslog syslog"$(date +"%Y%m%d_%T")"

echo "Copy Complete $date"

# End