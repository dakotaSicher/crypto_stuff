import tkinter as tk
from passwordDB import PasswordDatabase
from managerGui import loginGui, setMasterGui
import os
from os import path, stat

from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes, padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


iv = b"\x8e\x8d\xaa\x95a^*7\x19\xf3\xdd'\x07\xd40\xb2"
mysalt = b'\x7f\xd7\x8dkK\xaf\x02{5\xfc\x02\xf9\xcc}M.'

userPass = None
masterHash = None
userHash = None


#step 0: check if master password is set or set for first time
def masterExists():
    if(path.isfile('./master.txt') and stat('./master.txt').st_size != 0):
        return True
    return False

def getMaster():
    if(path.isfile('./master.txt') and stat('./master.txt').st_size != 0):
        file = open('./master.txt','rb')
        return bytearray(file.read())

def setMaster():
    while True:
        p1 = input("enter your new master password: ")
        p2 = input("confirm master password: ")
        if(p1 == p2): 
            break
    file = open('./master.txt','wb')
    h = hashes.Hash(hashes.SHA256())
    h.update(p1.encode())
    p = h.finalize() 
    file.write(p)  
    return p

#step 1: enter master password
def getUserHash(userPass):
    h = hashes.Hash(hashes.SHA256())
    h.update(userPass.encode())
    return h.finalize()
     

#step 3: generate key from master password
def genKeyFromMaster(pwd):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt = mysalt,
        iterations=480000
    )
    key = kdf.derive(pwd.encode())
    return key

def encryptPasswords(pt):
    padder = padding.PKCS7(256).padder()
    padded_password = padder.update(pt.encode())
    padded_password += padder.finalize()
    cipher = Cipher(algorithms.AES256(key), modes.CBC(iv))
    encryptor = cipher.encryptor()
    ct = encryptor.update(padded_password) + encryptor.finalize()
    return ct
    
def decryptPasswords(ct):
    cipher = Cipher(algorithms.AES256(key), modes.CBC(iv))
    decryptor = cipher.decryptor()
    dt = decryptor.update(ct) + decryptor.finalize()
    #print(dt)
    unpadder = padding.PKCS7(256).unpadder()
    pt = unpadder.update(dt)
    pt += unpadder.finalize()
    #print(plainpw.decode())
    return pt.decode()





if __name__ == "__main__":
    #retrieve hashed master password from file
    #or if none exists get new master password from user, hash and store
    if(masterExists()):
        loginGui(getMaster)
    else:
        setMasterGui(setMaster)
        




    #user inputs password to login
    #userPass = input("enter your password: ")
    #userHash = getUserHash(userPass)
    #print(masterHash.hex())
    #print(userHash.hex())
    #compare stored master password hash with user entered password hash
    if(userHash != masterHash):
        print("pasword does not match")
        time.sleep(2)
        exit
    else: 
        print("welcome back")
    
    key = genKeyFromMaster(userPass)
    pwmgr = PasswordDatabase()
    pwmgr.connect_or_create()

    site = "web.site"
    user = "user1234"
    dumbp = "pass1234"

    #ct = encryptPasswords(dumbp)
    #pwmgr.newCred(site,user,ct)


    cred = pwmgr.getCred(site)

    print(cred)
    #print(cred[1])
    
    

    pwmgr.closeConn()
    time.sleep(5)
