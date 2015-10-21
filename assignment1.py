K = 6174

print "\n*****Exercise 2*****"
def gt(x, y):
    return x > y
print ">>> gt(2,3)"
print gt(2,3)

print "\n*****Exercise 3*****"
def lt(x, y):
    return x < y
print ">>> lt(2,3)"
print lt(2,3)

print "\n*****Exercise 4*****"
def si(digits):
    if digits <= 0:
        return []
    else:
        return si(digits / 10) + [digits % 10]
print ">>> si(2538)"
print si(2538)

print "\n*****Exercise 5*****"
def bubble_sort(lst, func):
    num = -1
    while(num != 0):
        num = 0
        for i in range(0,len(lst)-1):
            if(func(lst[i],lst[i+1])):
                temp = lst[i+1]
                lst[i+1] = lst[i]
                lst[i] = temp
                num+=1
    return lst
print ">>> bubble_sort([2,5,3,8], lt)"
print bubble_sort([2,5,3,8], lt)
print ">>> bubble_sort([2,5,3,8], gt)"
print bubble_sort([2,5,3,8], gt)

print "\n*****Exercise 6*****"
def clti(lst):
    return int(''.join(str(e) for e in lst))

print ">>> clti([2,5,3,8])"
print clti([2,5,3,8])

print "\n*****Exercise 7*****"
def kaprekar(num):
    lst1 = []
    lst = list(str(num))
    for i in lst:
        lst1 += [int(i)]
    n1 = bubble_sort(lst1, lt)
    a1 = clti(n1)
    n2 = bubble_sort(lst1, gt)
    a2 = clti(n2)
    num1 =  a1 - a2
    if (num1 == K):
        return "Kaprekar constant reached"
    elif(num1 == 0):
        return 0
    else:
        return kaprekar(num1)

print ">>> kaprekar(8730)"
print kaprekar(8730)

print "\n*****Exercise 8*****"
def iterativeKaprekar(num):
    lst1 = []
    count = 1
    lst = list(str(num))
    for i in lst:
        lst1 += [int(i)]
    n1 = bubble_sort(lst1, lt)
    a1 = clti(n1)
    n2 = bubble_sort(lst1, gt)
    a2 = clti(n2)
    num1 =  a1 - a2
    while (num1 != K and num1 != 0):
        lst1 = []
        lst = list(str(num1))
        for i in lst:
            lst1 += [int(i)]
        n1 = bubble_sort(lst1, lt)
        a1 = clti(n1)
        n2 = bubble_sort(lst1, gt)
        a2 = clti(n2)
        num1 =  a1 - a2
        count+=1
    if (num1 == K):
        return "Kaprekar constant reached in " + str(count) + " iterations."
    elif(num1 == 0):
        return 0

print ">>> iterativeKaprekar(3524)"
print iterativeKaprekar(3524)
