# Script Name:      Windows Configuration Script
# Author:           marburgja
# Last Rev:         20211004
# Purpose:          Setup a new Windows endpoint machine

# Main

Disable-WindowsOptionalFeature -Online -FeatureName SMB1Protocol #Disables SMBv1
Set-ADDefaultDomainPasswordPolicy -ComplexityEnabled $True #Enables Password Complexity

# End