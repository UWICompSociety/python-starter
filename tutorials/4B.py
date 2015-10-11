print "\nTutorial 4B"

print "\nQuestion 1"


def strange(n):
    if n <= 1:
        return 0
    else:
        return 1 + strange(n / 3)


print "\nstrange if recursive because it calls references itself"

print "\nOutputs:"
print "strange(1) ->", strange(1)
print "strange(2) ->", strange(2)
print "strange(3) ->", strange(3)
print "strange(8) ->", strange(8)

print "\nThe order of growth is O(log n)"

print "\nQuestion 2"


