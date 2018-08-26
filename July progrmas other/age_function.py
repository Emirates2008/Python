def Age(a):
    b = a[4:]
    b = int(b)
    c = 2018 - b
    return c

def Pass18(a):
    if (a<18):
       return "You are to small to get a bank account.:("
    elif (a>110):
        return "You must be dead by now.:I"
    else:
        return "You are old enough to get a bank account.:)"
    
