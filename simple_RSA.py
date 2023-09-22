
def gcd(a,b):
    while a % b > 1:
        c = a % b
        a = b
        b = c
    return 

def EA(a,m): #does the inverse exist
    return

def EEA(a,m): #calculate the inverse
    return

def findNthPrimes(n):
    primeList = [2]
    next = 3
    while len(primeList) < n:
        for p in primeList:
            if next % p == 0 : break
        
        else: primeList.append(next)
        next += 2
    return primeList[-1]


if __name__=="__main__":
    p = input("enter the nth prime number: ")
    q = input("enter the mth prime number: ")