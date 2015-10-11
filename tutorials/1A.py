print "\nTutorial 1A"


def square(num):
    return num * num


print "\nQuestion 1",

print "65", type(65)
print "3.14", type(3.14)
print "65", type(65)
print "COMP1126", type("COMP1126")
print "True", type(True)
print "False", type(False)
print "COMPUTING", type("COMPUTING")

print "\nQuestion 2"

print "2 + 3 + 5", 2 + 3 + 5
print "'hello' + 'o'", 'hell' + 'o'
print "2 + 3 * 5**2", 2 + 3 * 5 ** 2
print "-4 + 2", -4 + 2
print "5 < 6", 5 < 6
print "not 5 == 6", 5 == 6
print "square(3) - 2 * 4 + square(2) + 3 < square(3)", square(3) - 2 * 4 + square(2) + 3 < square(3)

print "\nQuestion 3"

x = 5
y = 3
z = 40.5
a = x * y
x = a
b = x

print "a = %i\nb = %i\ny = %i\n y + 1 = %i\nint(z) = %i\nx + x = %i\na < x * x = %r\nb + 4 == a * x = %r" % (a, b, y, y + 1, int(z), x + x, a < x * x, b + 4 == a * x)

