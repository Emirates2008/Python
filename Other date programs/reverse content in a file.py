f=open("hello.txt",'r')
a = f.read()
print(a[::-1])
f.close()
