
char_set = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
            'n','o','p','q','r','s','t','u','v','w','x','y','z',
            '0','1','2','3','4','5','6','7','8','9','.',',','?']
l = len(char_set)

def generateKey(string, keyword):
    key = list(keyword)
    if len(string) == len(key):
        return(key)
    else:
        for i in range(len(string) -len(key)):
            key.append(key[i % len(key)])
    return("" . join(key))

def cipherText(string, key):
    cipher_text = []
    for i in range(len(string)):
        x=(char_set.index(string[i])+ char_set.index(key[i])) % l
        cipher_text.append(char_set[x])
    return("" . join(cipher_text))

def originalText(cipher_text, key):
    orig_text = []
    for i in range(len(cipher_text)):
        x = (char_set.index(cipher_text[i]) - char_set.index(key[i]) + l) % l
        orig_text.append(char_set[x])
    return("" . join(orig_text))

if __name__=="__main__":
    string = input("enter text to encrypt: ")
    keyword = input("enter keyword: ")
        
    string = string.lower()
    keyword = keyword.lower()
    key = generateKey(string, keyword)
    cipher_text=cipherText(string, key)
#    print(key)
    print(cipher_text)
    print(originalText(cipher_text, key))
