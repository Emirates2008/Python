desicion = "yes" 
while desicion  == "yes":
    print (' What mathematical operation do you want to do?'' Please enter +, -, *, /, or %?  % is division with a reaminder.')
    choice =input()
    if (choice=="+"):
        number1 = input()
        number2 = input()
        sum = int(number1) + int(number2)
        print(sum)
    
    elif (choice=="-"):
        number1 = input()
        number2 = input()
        diffrence =int(number1) - int(number2)
        print(diffrence)

    elif (choice=="*"):
        number1 = input()
        number2 = input()
        product = int(number1) * int(number2)
        print(product)

    elif (choice=="/"):
        number1 = input()
        number2 = input()
        quotient = int(number1) / int(number2)
        print (quotient)
    elif (choice=="%"):
        number1 = input()
        number2 = input()
        remainder = int(number1)%  int(number2)
        print (remainder)

    else: print("That is not a mathematical operation.")
    desicion = input("Do you want to continue?")

else:
    print("Thanks for using this calculator program called calcmath copyrighted by Tanush Chava on 6/14/2018.")
    
        
    
    
    
