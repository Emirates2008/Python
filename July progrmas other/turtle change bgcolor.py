from turtle import *
def blue_screen():
    bgcolor('blue')
    t.circle(134)

def white_screen():
    #t.hideturtle()
    bgcolor('red')

t=Turtle()
listen()
onkeypress(blue_screen, 'space')
onkeypress(white_screen,'space')
    
