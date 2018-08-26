classes = []
n = int(input(" How many students are in your class."))
i = 0
while(i < n):
         s=[]
         a = input("Pick the name of a student.")
         b = input("Enter the age of this student.")
         c = input("Enter the grade of this student.")
         s.append(a)
         s.append(b)
         s.append(c)
         classes.append(s)
         i = i + 1
         
print(classes)


for s in classes:
   if( s[2] =='1'):
        print(s)
    
