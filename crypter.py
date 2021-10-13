#! /usr/bin/env python3
# Script Name:      servercheck
# Author:           marburgja
# Last Rev:         20211012
# Purpose:          encrypt or decrypt a file
# Sources:          https://github.com/billkach/ops-challenges/blob/main/401ops06.py

# Libraries
import os
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

def print_options():
            print("0. Write a Key")
            print("1. Encrypt a File")
            print("2. Decrypt a File")
            print("3. Encrypt a String")
            print("4. Decrypt a String")
            print("5. Encrypt a File AND Contents")
            print("6. Decrypt a File AND Contents")
            print("7. Exit Menu")

def main():
    print_options()
    choice=input("Enter your choice [1-6]: ")

    if choice=="0":
        write_key()
        print("Key Created")

    elif choice=="1":
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

    elif choice=="3":
        key=load_key()
        f=Fernet(key)
        string=input("Enter String To Encrypt:")
        estring=string.encode()
        encrypted=f.encrypt(estring)
        print("Encrypted String:")
        print(str(encrypted))
        print(type(encrypted))
        time.sleep(2)

    elif choice=="4":
        key=load_key()
        f=Fernet(key)
        string=input("Enter String To Decrypt:")
        estring=string.encode()
        decrypted=f.decrypt(estring)
        print("Decrypted String:")
        print(decrypted)
        time.sleep(2)

    elif choice=="5":
        def recursive_encrypter(filename):
            key=load_key()
            f=Fernet(key)
            with open(filename, "rb") as file:
                file_data = file.read()
                encrypted_data = f.encrypt(file_data)
            with open(filename, "wb") as file:
                file.write(encrypted_data)

        enpath=input("Enter Filepath for Recursive Encryption:")
        for (root, dirs, filenames) in os.walk(enpath):
            for file in filenames:
                filename = os.path.join(root,file)
                recursive_encrypter(filename)
        print("Encryption Successful")
        


    elif choice=="6": 
        def recursive_decrypter(filename):
            key=load_key()
            f=Fernet(key)
            with open(filename, "rb") as file:
                encrypted_data = file.read()
                decrypted_data = f.decrypt(encrypted_data)
            with open(filename, "wb") as file:
                file.write(decrypted_data)
        depath=input("Enter Filepath for Recursive Decryption:")
        for (root, dirs, filenames) in os.walk(depath):
            for file in filenames:
                filename = os.path.join(root,file)
                recursive_decrypter(filename)


    elif choice=="7":
        exit

    else:
        print("Invalid Input")
        print_options()
# Main

main()

# End