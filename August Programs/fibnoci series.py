a = []
n = int(input("Enter how many numbers of hte fibnoci series you want me to print."))
FirstElement = 1
secondElement = 1
a.append(FirstElement)
a.append(secondElement)
for i in range(n-2):
    a.append(a[-1]+a[-2])
print(a)

filename = "Tanush Fibnoci File"
f=open(filename,'w')
f.write(str(a))
f.write("\n")
f.close()
