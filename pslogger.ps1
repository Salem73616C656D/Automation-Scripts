# Script Name:      Event Logger
# Author:           marburgja
# Last Rev:         20210508
# Purpose:          Show System Log Events/Print Events

# Variables

# Functions
get-eventlog system -after (get-date).addhours(-24) | format-table -wrap | out-file -filepath C:\Users\joshm\desktop\systemlogs.txt

get-eventlog system -after (get-date).addhours(-24) -entrytype error | format-table -wrap | out-file -filepath c:\users\joshm\desktop\errors.txt

get-eventlog system -after (get-date).addhours(-24) -instanceid 16 | format-table -wrap

get-eventlog system -newest 20 | format-table -wrap

get-eventlog system -newest 500 | select-object source


# Main


# End