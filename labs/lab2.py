#Question 1
def quadratic(a,b,c):
    discrim=(b**2)-4*a*c
    root1=(-1*b+discrim**.5)/(2*a)
    root2=(-1*b-discrim**.5)/(2*a)
    if discrim>=0:
        if root1>root2:
            return root1
        return root2
    else:
        print ("No real roots")

#Question 2
def check_fermat(a,b,c,n):
    if n<=0:
        print ("Error")
    elif n>2:
        if a**n+b**n==c**n:
            print("I made a discovery-Fermat was wrong")
            return False
        else:
            return True
    elif (n==1 or n==2):
        if (a**n+b**n==c**n):
            return True
        else:
            return False
    

#Question 3
"""def isPrime(n):
    for p in range(2,n):
        if n%p==0:
            return False
        return True
    if n==2:
        return True
    elif n==1:
        return False"""
    
#Question 4
def primes(x,y):
    def isPrime(n):
        for p in range(2,n):
            if n%p==0:
                return False
        return True
        if n==2:
            return True
        elif n==1:
            return False
    for s in range (x,y+1):
        if isPrime(s)==True:
            print (s)
