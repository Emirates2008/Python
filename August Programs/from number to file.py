a = []
a.append(int(input("Enter a number.")))
for i in range(4):
    a.append(int(input("Enter another number.")))
    
filename = "Numberfiletest.txt"
f=open(filename,'w')
f.write(str(a))
f.write("\n")
f.close()
