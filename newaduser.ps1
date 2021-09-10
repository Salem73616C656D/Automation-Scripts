# Script Name:      newaduser
# Author:           marburgja
# Last Rev:         20210909
# Purpose:          Creates new user in AD

# Main

New-ADUser `
-Name "Franz Ferdinand" `
-GivenName "Franz" `
-Surname "Ferdinand" `
-SamAccountName "f.ferdinand" `
-AccountPassword (Read-Host -AsSecureString "Input User Password") `
-ChangePasswordAtLogon $True `
-Company "GlobeX USA" `
-Title "TPS Reporting Lead" `
-State "Oregon" `
-City "Springfield" `
-Department "TPS" `
-EmailAddress "ferdi@GlobeXpower.com" `
-Enabled $True

# End

