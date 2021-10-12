from cryptography.fernet import Fernet

def print_menu():
    print ("1. ENCRYPT a FILE")
    print ("2. DECRYPT a FILE")
    print ("3. ENCRYPT a STRING")
    print ("4. DECRYPT a STRING")
    print ("5. Exit")



print_menu()
choice=input("Select An Option [1-5]:")

if choice==1:
    path=input("Enter Filepath:")
    key=Fernet.generate_key()
    with open('filekey.key', 'wb') as filekey:
        filekey.write(key)
    with open('filekey.key', 'rb'):
        key=filekey.read()
    fernet=Fernet(key)
    with open(path, 'rb') as file:
        original=file.read()
    encrypted=fernet.encrypt(original)
    with open(path, 'wb') as encrypted_file:
        encrypted_file.write(encrypted)
            
#    elif choice==2:
#        print()
#    elif choice==3:
#    elif choice==4:
#    elif choice==5:
#    else: