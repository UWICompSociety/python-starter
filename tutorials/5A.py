import math

print "\nTutorial 5A"

print "\nQuestion 1"


def my_sum1(start, stop):
    if start > stop:
        return 0
    else:
        return start + my_sum1(start + 1, stop)


def my_sum2(start, stop):
    if start > stop:
        return 0
    else:
        return 1.0 / start + my_sum2(start + 1, stop)


def my_sum3(start, stop):
    if start > stop:
        return 0
    else:
        return start ** 2 + my_sum3(start + 2, stop)


def sigma(term, start, nxt, stop):
    if start > stop:
        return 0
    else:
        return term(start) + sigma(term, nxt(start), nxt, stop)


print "\nPart B"
print "sigma(lambda k: 1/(k * (k + 1)), 1, lambda x: x+1, 100) ->", sigma(lambda k: 1 / (k * (k + 1)), 1,
                                                                          lambda x: x + 1, 100)
print "sigma(lambda k: 1 / k! , 0, lambda x: x+2, 50) ->", sigma(lambda k: 1 / math.factorial(k), 0, lambda x: x + 2,
                                                                 50)

print "\nQuestion 2"


def prod_series(start, stop):
    if start > stop:
        return 0
    else:
        return start ** 2 * prod_series(start + 1, stop)


print "2^2 * 3^2 * 4^2 * 5^2 * 6^2", prod_series(2, 6)


def prod_series2(start, stop):
    if start > stop:
        return 0
    else:
        return start ** 3 * prod_series2(start + 1, stop)


print "1^3 * 2^3 * 3^3 * 4^3 * 5^3", prod_series2(1, 5)

print "\nQuestion 3"


def linear(a, b):
    def result(x):
        return a * x + b

    return result


print "linear returns a higher order function that can be later executed"
print "linear(2, 10)(3) ->", linear(2, 10)(3)


def linear2(a, b):
    return lambda x: a * x + b


print "linear2 produces the same result as linear\n"
print "linear(1, 20)(3) ->", linear(1, 20)(3)
print "linear2(1, 20)(3) ->", linear2(1, 20)(3)
