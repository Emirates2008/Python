a = {"RB":[100,100,100],"B":[1,2,10],"H":[1,100,50],"Al":[12,32,1],"A":[98,100,13]}
b = input("Enter a student initial to reveal their marks.")
for key,value in a.items():
     if key==b:
         flag=1
     else:
        flag=0

if flag==1:
    print(a[b])
else:
    print("Not found")
