#Dakota Sicher
#simple program to encrypt text message using a one-time-pad of the same length
#
def applyPad(string, key):
    assert(len(string) == len(key))
    cipher = ""
    for i in range(len(string)):
        cipher = cipher + chr((ord(string[i])+ord(key[i]))%26 +ord('a'))
    return cipher
        

if __name__=="__main__":
    plainText = input("enter your plain text: ")
    pad = input("enter you one-time-pad: ")
    
    cipherText = applyPad(plainText, pad)
    print(cipherText)


