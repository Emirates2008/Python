print("Pick a 2 digit number.")
choice = input()
choice = int(choice)
quotient = choice / 10
print(type(quotient))
remainder = choice % 10
print("The quotient is " + str(quotient) + ", and the reamainder is " + str(remainder))
