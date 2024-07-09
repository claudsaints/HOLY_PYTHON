#event listener
from turtle import Turtle,Screen

maxy = Turtle()
screen = Screen()

def moving():
    maxy.forward(10)
def move_back():
    maxy.backward(10)
def right():
    nh = maxy.heading() - 10
    maxy.setheading(nh)
def left():
    nh = maxy.heading() + 10
    maxy.setheading(nh)
def clear():
    maxy.clear()
    maxy.penup()
    maxy.home()
    maxy.pendown()


screen.listen()

screen.onkeypress(fun=right, key="d")
screen.onkeypress(fun=left, key="a")
screen.onkey(fun=moving, key="w")
screen.onkey(fun=move_back,key="s")
screen.onkey(fun=clear,key="space")
screen.exitonclick()



