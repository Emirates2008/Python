import math
import random
#Prog.1
#Print factorials of a number
def factorials(n):
    '''Function to find factorial'''
    return math.factorial(n)

#Prog.2
#Print area of square
def AreaSquare(a):
    '''Calculation to find area'''
    b = a*a
    return "The area of your square is " + str(b)

#find perimemter of square
def PerimeterSquare(s):
    a = s*4
    return "the perimeter of your square is " + str(a)
#Prog.3
#Find min and max of numbers in a list
def Min_Max(a):
    '''Finding least number, then greatest one'''
    return min(a),max(a)
    
#Prog.4
def Sum(a):
    sum = 0
    '''In other words, the func. will go through all the numbers,
and will keep on adding the numbers to sum.'''
    for i in a:
        sum = sum+i
    return sum
#Prog.5
#def SecondLargest(a):
   # a.sort()
   # return a[-2]

#Prog.6
#def Remove_Duplicates(l):
    #return set(l)


#Prog.7
#Print prime numbers between 1000,2000
def Prime10002000():
    for i in range(1000,2000):
        if (isPrime(i)):
                return i 

#Prog.8
#Prog. to reverse a number
def ReverseNum(num):
    reverse = 0 
    while(num>0):
        quotient=num//10
        remainder = num % 10
        num=quotient
        reverse = reverse*10 + remainder
    return reverse

#Prog.9
#Prog. to generate a random number.
def RandomNumber(a):
    print("I will generate a random number between 0 and 10000000000000000000000000000000000000000000000000000000000.")
    a = random.randrange(0,10000000000000000000000000000000000000000000000000000000000)
    return a    

    
    




    



