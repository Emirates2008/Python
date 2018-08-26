def StrCount(a):
    acount = 0
    for characters in a:
        acount = acount + 1
    return acount
a = "Here's Joe Cool hanging around the dome on a sunday."
b = StrCount(a)
print(b)



a = [1,2,3,5,8,13,21,34,55,89]
b = [1,2,3,4,5,6,7,8,9,10,11,12,13]
c = a+b
d=[]
for element in c:
    z  = c.count(element)
    if(z>1 and element not in d):
        d.append(element)
print(d)


a = [1,2,3,5,8,13,21,34,55,89]
b = [1,2,3,4,5,6,7,8,9,10,11,12,13]
c = []
for element in a:
    if element in b:
        c.append(element)
print(c)

