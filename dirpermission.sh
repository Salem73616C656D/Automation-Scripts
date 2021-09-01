# Script Name:      dirpermission
# Author:           marburgja
# Last Rev:         20210901
# Purpose:          bulk changes permissions by directory

# Variables


# Functions
bulkperchange(){
    cd $path
    chmod -R $per $path
    ls -l
}
# Main
echo "Enter Directory Path:..."
read path
echo "Enter Desired Permissions (e.g. 777):..."
read per
bulkperchange

# End