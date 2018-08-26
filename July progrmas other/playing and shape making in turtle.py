import turtle
a = ["red", "blue", "yellow"]
a=a*12
t = turtle.Screen()
t.bgpic("C:\\eSupport\\bg.gif")
l=turtle.Turtle()
l.shape("turtle")
l.color("orange")
l.begin_fill()
l.pencolor("blue")
for i in range(34):
    l.pensize(134)
    l.pencolor(a[i])
    l.forward(57)
    l.left(57)
l.end_fill()    
