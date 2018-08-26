min = input("Pick a number.")
max = input("Pick a number,greater, then the other number, 10 numbers or more apart.")
car = int(min)
if(car%2==0):
    while(car < int(max)):
        print (car)
        car = car+2
else:
    while(car < int(max)):
        print (car)
        car = car+2
