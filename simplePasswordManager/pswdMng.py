import tkinter as tk
import sqlite3
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

#step 0: check if master password is set
def openMasterHash():
    return

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


