from turtle import Screen,Turtle
import time
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Anaconda")
#frames first step
screen.tracer(0)

snake = Snake()
#call constrols
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")



#call the move
game_is_on = True
while game_is_on:
    screen.update()
    #seconda delay to update
    time.sleep(0.5)
    snake.move()





screen.exitonclick()