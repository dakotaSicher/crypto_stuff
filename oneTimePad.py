#Dakota Sicher
#CS 47205
#simple program to encrypt text message using a one-time-pad of the same length
#
def applyPad(string, key):
    assert(len(string) == len(key))
    cipher = ""
    for i in range(len(string)):
        cipher = cipher + chr((ord(string[i]) + ord(key[i]) - 2*ord('a'))%26 + ord('a'))
    return cipher

def decrypt(string, key):
    assert(len(string) == len(key))
    plain = ""
    for i in range(len(string)):
        plain = plain + chr((ord(string[i]) - ord(key[i]))%26 +ord('a'))
    return plain


if __name__=="__main__":
    plainText = input("enter your plain text: ")
    pad = input("enter you one-time-pad: ")
    
    cipherText = applyPad(plainText, pad)
    print(cipherText)
    print(decrypt(cipherText, pad))


