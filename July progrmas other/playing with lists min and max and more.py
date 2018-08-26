a = []
n = int(input("How many elements do you want in the list?"))
i=0
while(i<n):
        a.append(int(input("Pick a number.")))
        i=i+1
a.sort()
print(min(a))
print (max(a))

