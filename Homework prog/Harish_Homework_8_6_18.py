#Prog.1
#Print numbers of fibnoci series and save to a file.
a = []
n = int(input("Enter how many numbers of the fibnoci series you want me to print."))
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

#Prog.2
#Send even numbers in a list to a file.
even_list = []
firstask = int(input("Enter a number."))
i = 0
for i in range(11):
    even_list.append(int(input("Enter another number.")))
print(even_list)
evenfilename = "Tanush even save to file"
e = open(evenfilename,'w')
e.write(str(even_list))
e.write("\n")
e.close()
#Prog.3
#See how you can open a file by using its path.
import os
os.system("del #filename# ")
#os.rmdir("C:\Users\Tanush\Desktop\Python\July progrmas other")

#Prog.4
#Print area of rectangle and send to file
a = float(input("Choose the length of your rectangle."))
b = float(input("Choose the width of your rectangle."))
s = a * b
print("The area of your rectangle is " + str(s))
area_of_rectangle_file_name = "Tanush area of rectangle save to file"
area = open(area_of_rectangle_file_name,'w')
area.write(str(s))
area.write("\n")
area.close()








