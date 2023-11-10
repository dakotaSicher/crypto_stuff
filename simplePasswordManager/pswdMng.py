import tkinter as tk
import sqlite3
import sys
from os import path, stat
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


#window = tk.Tk()

#step 0: check if master password is set or set for first time
def getMaster():
    if(path.isfile('./master.txt') and stat('./master.txt').st_size != 0):
        file = open('./master.txt','rb')
        master = bytearray(file.read())
    else:
        master = newMasterHash()
    return master

def newMasterHash():
    print("getting new password")
    #get user input from gui
    newPassword = "password1234"
    file = open('./master.txt','wb')
    h = hashes.Hash(hashes.SHA256())
    h.update(newPassword.encode())
    p = h.finalize() 
    file.write(p)  
    return p

#step 1: enter master password
def getUserPass():
    return

#step 2: hash and compare to stored master password hash
def authPass():
    return

#step 3: generate key from master password
def pwdKeyGen():
    return

#step 4: open password database
def openPwdDB():
    return

#setp 5: options: view, add, delete

if __name__ == "__main__":
    pswHash = getMaster()
    print(pswHash.hex())
    time.sleep(2)
