# Script Name:      Windows Configuration Script
# Author:           marburgja
# Last Rev:         20210809
# Purpose:          Setup a new Windows endpoint machine

# Variables
# defined in section*

# Functions

# Main

# Enable File And Printer Sharing
Set-NetFirewallRule -DisplayGroup "File And Printer Sharing" -Enabled True -Profile Any

# Allow ICMP Traffic
New-NetFirewallRule `
-Name 'ICMPv4' `
-DisplayName 'ICMPv4' `
-Description 'Allow ICMPv4' `
-Profile Any `
-Direction Inbount `
-Action Allow `
-Protocol ICMPv4 `
-Program Any `
-LocalAddress Any `
-RemoteAddress Any `

# Enable Remote Management
Set-NetFirewallRule -DisplayGroup "Remote Desktop" -Enabled True -Profile Any

# Remove Bloatware
Get-AppxPackage *skypeapp* | Remove Remove-AppxPackage
Get-AppxPackage *3dbuilder* | Remove Remove-AppxPackage
Get-AppxPackage *windowscommunicationsapps* | Remove Remove-AppxPackage
Get-AppxPackage *windowscamera* | Remove Remove-AppxPackage
Get-AppxPackage *zunemusic* | Remove Remove-AppxPackage
Get-AppxPackage *windowsmaps* | Remove Remove-AppxPackage
Get-AppxPackage *solitairecollection* | Remove Remove-AppxPackage
Get-AppxPackage *bingfinance* | Remove Remove-AppxPackage
Get-AppxPackage *zunevideo* | Remove Remove-AppxPackage
Get-AppxPackage *bingnews* | Remove Remove-AppxPackage
Get-AppxPackage *onenote* | Remove-AppxPackage
Get-AppxPackage *people* | Remove-AppxPackage
Get-AppxPackage *windowsphone* | Remove-AppxPackage
Get-AppxPackage *windowsstore* | Remove-AppxPackage
Get-AppxPackage *bingsports* | Remove-AppxPackage
Get-AppxPackage *soundrecorder* | Remove-AppxPackage
Get-AppxPackage *bingweather* | Remove-AppxPackage
Get-AppxPackage *xboxapp* | Remove-AppxPackage

# Enable Hyper-V
$hyperv=Get-WindowsOptionalFeature -Online -FeatureName Microsoft-Hyper-V-All

if($hyperv.State -eq "Enabled") {
    Write-Host "Hyper-V Is Enabled."
} else {
    Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Hyper-V -All
}

# Disable SMBv1
$smb=Get-WindowsOptionalFeature -Online -FeatureName smb1protocol

if($smb.State -eq "Disabled") {
    Write-Host "SMBv1 Is Disabled."
} else {
    Disable-WindowsOptionalFeature -Online -FeatureName Microsoft-Hyper-V -All
}

# End 