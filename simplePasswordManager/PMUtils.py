from os import path, stat

from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes, padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

iv = b"\x8e\x8d\xaa\x95a^*7\x19\xf3\xdd'\x07\xd40\xb2"
mysalt = b'\x7f\xd7\x8dkK\xaf\x02{5\xfc\x02\xf9\xcc}M.'

def masterExists():
    if(path.isfile('./master.txt') and stat('./master.txt').st_size != 0):
        return True
    return False

def getMaster():
    if(path.isfile('./master.txt') and stat('./master.txt').st_size != 0):
        file = open('./master.txt','rb')
        return bytearray(file.read())

def setMaster(p1):
    file = open('./master.txt','wb')
    h = hashes.Hash(hashes.SHA256())
    h.update(p1.encode())
    p = h.finalize() 
    file.write(p)  
    print("new password saved")
    return p

def getUserHash(userPass):
    h = hashes.Hash(hashes.SHA256())
    h.update(userPass.encode())
    return h.finalize()
     
def genKeyFromMaster(pwd):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt = mysalt,
        iterations=480000
    )
    key = kdf.derive(pwd.encode())
    return key

def encryptPasswords(pt, key):
    padder = padding.PKCS7(256).padder()
    padded_password = padder.update(pt.encode())
    padded_password += padder.finalize()
    cipher = Cipher(algorithms.AES256(key), modes.CBC(iv))
    encryptor = cipher.encryptor()
    ct = encryptor.update(padded_password) + encryptor.finalize()
    return ct
    
def decryptPasswords(ct, key):
    cipher = Cipher(algorithms.AES256(key), modes.CBC(iv))
    decryptor = cipher.decryptor()
    dt = decryptor.update(ct) + decryptor.finalize()
    unpadder = padding.PKCS7(256).unpadder()
    pt = unpadder.update(dt)
    pt += unpadder.finalize()
    return pt.decode()




