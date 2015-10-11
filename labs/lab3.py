#Question 1
def power(n):
    if n<=0:
        return 0
    else:
       return (n**n)

#Question 2
def sumSeries(n):
    if n<=0:
        return 0
    else:
        return power(n) + sumSeries(n-1)

#Question 3
#part a
def div(x,y):
    if x<y:
        return 0
    else:
        return div(x-y,y)+1

#part b
def mod(x,y):
    if x<y:
        return x
    else:
        return mod(x-y,y)

#Question 4

def lastDigit(x):
     return mod(x,10)
    
def allButLast(x):
    return div(x,10)

def sumDigits(x):
    if x<=0:
        return 0
    else:
        return sumDigits(allButLast(x)) + lastDigit(x)




#Question 5

def is_valid(x):
    if x>=1000 and x<=6999:
        if sumDigits(x)%7==0:
            return True
        else:
            return False
    else:
        return False