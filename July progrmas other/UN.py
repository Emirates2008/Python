from b import *
a = []
b = []
n = int(input("How many elements do you want in each of your lists."))
for element in range(n):
        x=int(input("Enter a number to add to the a list."))
        a.append(x)
        y=int(input("Enter a number to add to the b list."))
        b.append(y)`
print(Common(a,b))
