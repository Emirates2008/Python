#Problem no.1
#If you give me your age, I will calculate when you will be a 100 years old.
name = input("What is your name?")
age = int(input("What is your age?"))
when = 2018 - age
you = when + 100
print(str(name) + ", you will be 100 years old in the year " + str(you) + ".")

#Problem no.2
# Question = "What is one function to output content to the console in Python?"
# Choices: echo, output, print, or, console.log
# My answer = "print"

# Problem no.3
# I don't understand what a quadratic equation is.
# Will you please explain it to me next class?

# Problem no.4
#Question = What is the value of x after these commands execute?
#Commands:
# x = 10
#x = x + x
#x = x - 5
#My answer = x = 10, 10 + 10 = 20, 20 - 5 = 15
#Final answer = x = 15

#Problem no.5
print("You have completed a bike race that went up a hill, and down a hill." "It is divided into the 2 parts." " You will be graded on your average speed for the whole race.")
a = float(input("What was the distance of the uphill part of the race?; measured in km."))
b = float(input("What was the distance of the downhill part of the race?; measured in km."))
c = float(input("How long did it take you to complete the uphill part of the race?; measured in min."))
d = float(input("How long did it take you to complete the uphill part of the race?; measured in min."))
Totaldistance = a + b
Totaltime = c + d
Averagespeed = Totaldistance / Totaltime
print("Your average speed for the entire race was " + str(Averagespeed) + " minutes.")

#Problem no.6
#Write your own turtle program with AMAZING stuff.

import turtle
a = ["SeaGreen2", "PaleGoldenrod", "PowderBlue", "MistyRose2", "MediumAquamarine", "VioletRed4"]
a = a*10

t = turtle.Screen()
l=turtle.Turtle()
turtle.mode("logo")
turtle.speed(10)
turtle.shape("turtle")
l.shape("turtle")
l.bgcolor = ("LemonChiffon3")
l.fillcolor("HotPink")
for i in range(19):
    l.pensize(6)
    l.pencolor(a[i])
    l.forward(300)
    l.left(256)
    


l.penup()
l.goto(-367,56)
l.pencolor("gainsboro")
l.pendown()
for i in range(13):
    l.forward(600)
    l.right(210)


l.penup()    
l.goto(378, -45)
l.pencolor("cornsilk3")
l.pendown()
l.begin_fill()
l.circle(134)
l.end_fill()
l.stamp()
l.clearstamp()

#Problem no.7
#A program to sort the names of students in alphabetical order.
a = []
b = int(input("How many student names do you want for me to put in my list?"))
i = 0
while(i<b):
    a.append(input("Enter a student name ; only the first name."))
    i = i+1. 

a.sort()
print("I will print these given names in alphabetical order.")

print(a)
#Problem no.8
#Write algorithms to check if a number is even or odd. Refer to the program that we had done earlier.
#Me or my brother do not have the program to refer to. I don't know if we even did that program with you, or anybody else.
# I can try writing an algorithm, though.
#algoritm = Input a number from the user, using the input function. If the number can be divided by 2 with a remaindeer of 0, it is even. Else, odd.

