import random
import math
import sys

#meed a > b
def gcd(a,b):
    while  b != 0:
        c = a % b
        a = b
        b = c
    return a

#need a > b
def EA(a,b): #does the inverse exist
    if (gcd(a,b) == 1): return True
    return False

#need: m > a 
#calculate the inverse 
#my lazy version of extended euclidian algo
def findInv(a,m): 
    inv = -1
    if(not EA(m,a)): return inv #gcd = 1 
    # need to solve 1 == i*m + t*a => t+m = inv
    i = 1
    t = -int(m/a)
    while (i*m + t*a != 1):
        i += 1
        t = -int(m*i/a)

    inv = t + m
    return inv

primeList = [2,3]

def findNthPrimes(n):
    if(n < len(primeList)): return primeList[n-1] #is the nth prime already in our list
    next = primeList[-1] + 2 #next odd number after last prime in our list
    #go until we get to the nth prime
    while len(primeList) < n:
        for p in primeList:
            if next % p == 0 : break    #check if each prime is a factor of next
        
        else: primeList.append(next)    #if no prime factors then next is also prime
        next += 2 # dont' need to check even numbers
    return primeList[-1]

#uses phi n and the generated primes list to pick a value that is < phi-1
def pickPub(phi_n):
    #find prime factors of %
    i = 0
    phiFactors = []
    limit = math.sqrt(phi_n)
    num = phi_n
    while(primeList[i] < limit): # upper limit for prime factor for a number is the square root of the number 
        if(num%primeList[i] == 0): 
            phiFactors.append(primeList[i])
            num = num/primeList[i]
        else: i += 1
    print(phiFactors)
    #easy answer is pick a prime number that is not a prime factor of Phi and less than phi
    #need to make sure we have all the primes up to phi
    while(primeList[-1] < phi_n):
        findNthPrimes(len(primeList)+1)
    
    #options for pub key are [2, phi-2] and coprime with phi
    #any prime number that is not a prime factor of phi will do
    options = []
    j = 0
    while(primeList[j] < phi_n):
        if primeList[j] not in phiFactors:
            options.append(primeList[j])
        j +=1
    print(options)
    #options = the set of prime numbers up to phi not including the prime factors of phi
    return options[random.randint(0,len(options)-1)]


def encrypt(m, e, n):
    s = []
    for l in m:
        x = ord(l)
        y = x**e % n
        s.append(y)
    return s

def decrypt(c, d, n):
    s = ""
    for y in c:
        x = y**d % n
        if(n<127): s = s+chr(x+n)
        else: s = s + chr(x)
    return s


if __name__=="__main__":
    p = int(input("Enter the nth prime number: "))
    q = int(input("Enter the mth prime number: "))
    message = input("Enter message to encrypt: ")
    p = findNthPrimes(p)
    q = findNthPrimes(q)
    n = p*q
    phi_n = (p-1)*(q-1)
    e = pickPub(phi_n)
    assert gcd(e,phi_n) == 1
    d = findInv(e,phi_n)
    assert e*d % phi_n == 1

    print("Public  Key = (",e,", ", n, ")")
    print("Private Key = (",d,", ", n, ")")

    c = encrypt(message,e,n)
    print(c)

    print(decrypt(c,d,n))