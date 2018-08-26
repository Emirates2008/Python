
def UnuE():
    a = [1,2,2,3,4,4,5,6,6]
    unu = []
    u = []
    for i in a:
        e = a.count(i)
        if(e > 1):
            unu.append(i)
        else:
            u.append(i)
    print(unu)
    print(u)
print(UnuE())
