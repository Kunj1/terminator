import random
import math

def check(x):
    s=str(x)
    l=len(s)
    sum=0
    if (l%2)==1:
        g=0
        h=1
    elif (l%2)==0:
        g=1
        h=0
    for i in range(h,l-1,2):
        a=int(s[i])
        sum=sum+(a*2)
    for i in range(g,l,2):
        a=int(s[i])
        sum=sum+a
    if (sum%10)==0:
        return 0
    else:
        return 1  

def mastercard(L):
    c=1
    while(c==1):
        n=random.randint(51*math.pow(10,14),(56*math.pow(10,14))-1)
        c=check(n)
        if c==1:
            continue
        if n in L:
            c=1
    return n

def visa(L):
    c=1
    while(c==1):
        b=random.randrange(13,17,3)
        n=random.randint(4*math.pow(10,b-1),(5*math.pow(10,b-1))-1)
        c=check(n)
        if c==1:
            continue
        if n in L:
            c=1
    return n

#example:
#list=[12412314124,4123412414,12414134124,124124124124124]
#number1=(mastercard(list))
#number2=(visa(list))
