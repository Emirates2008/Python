#This is a program to find the common elements in 2 lists.
def Common(a,b):
    a = set(a)
    b = set(b)
    '''Common Elements from two sets'''
    k = a.intersection(b)
    return k
