#! /usr/bin/env python3
# Script Name:      servercheck
# Author:           marburgja
# Last Rev:         20211011
# Purpose:          encrypt or decrypt a file

# Libraries.
import time
from cryptography.fernet import Fernet

# Variables

# Functions
def write_key():
    """
    Generates a key and save it into a file
    """
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    """
    Loads the key from the current directory named `key.key`
    """
    return open("key.key", "rb").read()

def main():
            print("1. Encrypt a file")
            print("2. Decrypt a file")
            print("3. Encrypt a message")
            print("4. Decrypt a message")
            print("5. Exit Menu")
            time.sleep(1)

# Main
main()
choice=input("Enter your choice [1-5]: ")

if choice=="1":
    key=load_key()
    f=Fernet(key)
    time.sleep(1)
    path=input("Enter Filepath:")
    time.sleep(1)
    with open(path, "rb") as file:
        file_data=file.read()
        encrypted_data=f.encrypt(file_data)
    with open(path, "wb") as file:
        file.write(encrypted_data)
        time.sleep(1)
    print("Encryption Successful")
    main()

elif choice=="2":
    key=load_key()
    f=Fernet(key)
    write_key()
    path=input("Enter Filepath:")
    with open(path, "rb") as file:
        encrypted_data=file.read()
        decrypted_data=f.decrypt(encrypted_data)
    with open(path, "wb") as file:
        file.write(decrypted_data)
    print("Decryption Successful")
    main()

elif choice=="3":
    key=load_key
    f=Fernet(key)
    string=input("Enter String To Encrypt:")
    estring=string.encode()
    encrypted=f.encrypt(estring)
    print("Encrypted String:")
    print(encrypted)
    time.sleep(2)
    main()

elif choice=="4":
    key=load_key
    f=Fernet(key)
    string=input("Enter String To Decrypt:")
    estring=str.encode(string)
    decrypted=f.decrypt(estring)
    print("Decrypted String:")
    print(decrypted)
    time.sleep(2)
    main()

elif choice=="5":
    exit

else:
    print("Invalid Input")
    main()

# End