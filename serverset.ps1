# Script Name:      serverset
# Author:           marburgja
# Last Rev:         20211007
# Purpose:          Configure CIS controls on new server

# Main

Disable-WindowsOptionalFeature -Online -FeatureName SMB1Protocol #Disables SMBv1
Set-ADDefaultDomainPasswordPolicy -ComplexityEnabled $True #Enables Password Complexity

# End
