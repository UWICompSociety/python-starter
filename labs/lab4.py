#Question 1
def encode(x):
    if x=="":
        return ""
    else:
        return chr(ord(x[0])+5)+encode(x[1:])

def decode(x):
    if x=="":
        return ""
    else:
        return chr(ord(x[0])-5)+decode(x[1:])
        
#Question 2
def square(x):
    return x**2
def cube(x):
    return x**3

def sumlist(x,f):
    sume=0
    for i in x:
        sume+=f(i)
    return sume

#Question 3

def mean(x):
    if x==[]:
        return 0
    else:
        return (sumlist(x,lambda x:x))/len(x)

#Question 4
import math
def std_dev(x):
    def variance(x):
        if x==[]:
            return 0
        else:
            return (sumlist(x,square)/len(x))-(mean(x))**2
    return math.sqrt(variance(x))