q = input("pick a number.")
q = int(q)
m = 2
flag=0
while(m < q):
    if(q % m ==0):
        flag = 1
    m = m+1

if (flag==0):
    print("This number is a prime.")
else:
    print ("This number is not a prime")
