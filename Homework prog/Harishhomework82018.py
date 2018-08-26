#Prog.1
#Reverse a string

a = "The Hennesy Venom F5 is the fastest car in the world, reaching speeds at 301mph."
def ReverseString(a):
    return a[::-1]
print(ReverseString(a))

#Prog.2
#Square and cube the second and third largest elements in a list.
a = [1,3,2,7,6,4,9,10,5,8]
a.sort()
def SC2(a):
    b = a[-2]
    c = a[-3]
    return b*b,b*b*b,c*c,c*c*c
x,y,p,q=SC2(a)
print(x)
print(y)
print(p)
print(q)
    
#Prog.3
#Find the unique and non-unique elements in a list
def UnuE(a):
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
a=['hello','Hello','Python']
print(UnuE(a))
#Prog.4
