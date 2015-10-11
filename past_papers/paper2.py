# quadratic equations general form below
# ax^2 + bx + c = 0



def close(x, y):
    # difference = x - y
    # absolute = abs(difference)
    # if absolute < 0.0001:
    #     return True
    # else:
    #     return False

    return abs(x - y) < 0.0001


def sqroot(radicand, guess):
    if close(radicand, guess ** 2):
        return guess
    else:
        # guess = (guess + radicand / guess) / 2
        # print sqroot(radicand, (guess + (radicand / guess)) / 2)
        return sqroot(radicand, (guess + (radicand / guess)) / 2)

def discriminant(a, b, c):
    return b**2 - 4 * a * c

def getR1(b, discrim, divConst):
    return (- b + sqroot(discrim, 1)) / divConst

def getR2(b, discrim, divConst):
    return (- b - sqroot(discrim, 1)) / divConst

def solveQuad(a, b, c):
    d = discriminant(a,b,c) # d -> discriminant
    divConst = 2 * a
    if d > 0:
        return getR1(b, d, divConst), getR2(b, d, divConst)
    elif d == 0:
        print getR1(b, d, divConst)
    else:
        print "No real roots"

print sqroot(2, 1.0)
# solveQuad(1, 3, 1)
