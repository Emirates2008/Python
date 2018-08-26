l=[[90,56,89,56,77],[100,100,60,40,50],[70,72,76,78,67]]
("Enter which subject you want me to order th lists base on.")
c=int(input("1.Math 2.Science 3.Arts 4.History 5.Music. Enter 0,1,2,3.or4"))
l.sort(key=lambda x:x[c])
print(l)
