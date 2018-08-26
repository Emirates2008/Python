import math
def Sum(a,b):
    d=a+b
    return d
print("Now to add 2 numbers.")
a=float(input("Enter A"))
b=float(input("Enter B"))

e=Sum(a,b)
print(e)

def Square(j):
    k = j ** 2
    return k
print("Now to square a number.")
j = float(input("Pick a number."))
    
m = Square(j)
print (m)

def Cube(num):
    c  = num **3
    return c
print("Now to cube a number.")
num = float(input("Pick a number."))
    
h  = Cube(num)
print (h)


def Multi(n,o):
    p = n*o
    return p
print("Now for multiplication.")
n=float(input("Enter N"))
o=float(input("Enter O"))
q = Multi(n,o)
print(q)

def Division(aa,bb):
    cc = aa/bb
    return cc
print("Now for some division.")
aa=float(input("Enter a number"))
bb=float(input("Enter another smaller number. "))
dd = Division(aa,bb)
print(dd)

def SqRoot(jj):
    ll = math.sqrt(jj)
    return ll
print("Now for the square root solver.")
jj=int(input("Enter a number; I will find the square root of it."))
zz = SqRoot(jj)
print(zz)


def Power(x,w):
    z=pow(x,w)
    return z
print("Now to find the power of a number.")
x=float(input("Enter X; the number"))
w=float(input("Enter W; the power to which you want to do the number to."))

y=Power(x,w)
print(y)
