 #I will input the multi table number from the user.
#Then, I will make a table
a = int(input("Pick a number for me to make a multiplication table out of."))
i = 0
while(i<=10):
   print( str(a) + " * " + str(i) + " = "  + str(a* i) + "\n")
   i = i+1
# now for it to appear backwards.
a = int(input("Pick a number for me to make a multiplication table out of backwards."))
i = 10
while(i>=0):
    print( str(a) + " * " + str(i) + " = "  + str(a* i) + "\n")
    i = i-1
