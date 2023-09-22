c=['u','d','e','h','k']
a_inv,b=9,5 
for i in range(len(c)):
    y=ord(c[i])-ord('a')
    #print(y)
    x=a_inv*(y-b)%26
    #print(x)
    print(chr(x+ord('a')))
