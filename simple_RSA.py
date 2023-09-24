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

#need: m > r 
#calculate the inverse 
#my lazy version of extended euclidian algo
def findInv(r,m): 
    inv = -1
    if(not EA(m,r)): return inv #gcd = 1 
    # need to solve 1 == i*m + t*a => t+m = inv
    q = 1
    t = -int(m/r)
    while (q*m + t*r != 1):
        q += 1
        t = -int(m*q/r)

    inv = t + m
    return inv

#Euler's Theroem 
#a ^ phi(n) = 1 mod n  =>
#a_inv = a^(phi(n)-1) mod n
#phi(n) = PRODUCT(p^e - p^(e-1) ) where p is a prime factor of n and e is the exponent(or number of times it is a prime factor) 
def EulerTheorem(r,m):
    inv = -1
    if(not EA(m,r)): return inv
    exp = []
    factors = phiFactors
    exp.append(1)
    i = 1
    phi = 1
    while(i < len(factors)):
        if(factors[i] == factors[i-1]):
            exp[i-1] += 1
            factors[i].pop()
        else:
            exp.append(1)
            phi *= (factors[i-1]**exp[i-1]- factors[i-1]**(exp[i-1]-1))
            i += 1
    inv = r**phi % m
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
phiFactors = []

def pickPub(phi_n):
    # upper limit for prime factor for a number is the square root of the number 
    limit = math.sqrt(phi_n)
    num = phi_n
    i = 0
    while(primeList[i] < limit): 
        if(num%primeList[i] == 0): 
            phiFactors.append(primeList[i])
            num = num/primeList[i]
        else: i += 1
    #print(phiFactors)
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
    #print(options)
    #options = the set of prime numbers up to phi not including the prime factors of phi
    return options[random.randint(0,len(options)-1)]

#problem occurs when n is too small (less than 127 I THINK) 
#results in decrypted message not being right in the cases
#already tried adding back in n to the final decrypted integers to get the correct ascii value but its not 100%
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
    assert EulerTheorem(e,phi_n) == d
    assert d != -1
    assert e*d % phi_n == 1

    print("Public  Key = (",e,", ", n, ")")
    print("Private Key = (",d,", ", n, ")")

    c = encrypt(message,e,n)
    print(c)
    
    m_out = decrypt(c,d,n)
    assert m_out == message
    print(m_out)