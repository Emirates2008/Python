number1 = float (input("enter the first number"))
number2 = float (input("enter the second number"))
number3 = float (input("enter the third number"))
if (number1 > number2) and (number1 > number3):
    largestnumber = number1
elif (number2 > number1) and (number2 > number3):
    largestnumber = number2
else: largestnumber = number3
print("the largest number is " + str(largestnumber))
