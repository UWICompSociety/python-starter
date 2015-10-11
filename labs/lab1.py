def mystery():
    dig = input("Please enter the last digit of your cellphone number :")
    dig = int(dig)
    b_year = input("Please enter your birth year :")
    b_year = int(b_year)
    l = (dig * 2 + 5) * 50 + 1765
    l -= b_year
    return l

def fuzzbiz():
    x = input("input number")
    x = int(x)
    if x % 3 == 0 and x % 5 == 0:
        return "FuzzBiz"
    elif x % 3 == 0:
        return "Fuzz"
    elif x % 5 == 0:
        return "Biz"
    else:
        return "No Fuzz No Biz"


def isLeapYear():
    lyear = input("input year")
    lyear = int(lyear)
    if lyear % 4 == 0 and lyear % 100 != 0:
        return True
    elif lyear % 400 == 0:
        return True
    else:
        return False
