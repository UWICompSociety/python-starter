import math

def digits(num):
    if num % 10 == 0:
        return 0
    else:
        return 1 + digits(num / 10)


def lcs(num):
    deci = 10
    head = 0
    tail = 0
    while num / deci > 0:
        head = num / deci
        tail = num % deci
        deci *= 10
    return tail * 10 + head

def isPrime(num):
    # we find the root
    root = math.sqrt(num)

    for i in range(2, root + 1):
        if num % i == 0:
            return False
    return True


print "digits(123) ->", digits(123)
print "lcs(197) ->", lcs(197)
print "isPrime -"
