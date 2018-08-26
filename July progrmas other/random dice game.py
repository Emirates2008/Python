import random
for i in range(3):
    a = int(input("Choose a number between 1 and 6."))
    b = random.randrange(1,6)
    if (b==a):
            print("You won the game; you guessed the number.")
    else:
            print("You lost; better luck next time.")


a  = [24,32,1,42,1,24,32,52,52,72,42,41,72]
for elements in a:
    c =  a.count(elements)
    if (c == 1):
        print("The unique number in the list is " + str(elements) + ".")
        

