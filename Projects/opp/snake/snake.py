from turtle import Turtle,Screen
screen = Screen()

# segments blocks in screen 
INIT_POSI = [(0,0),(-20,0),(-40,0)]
MOVE_DIST = 20
#degree
UP = 90
DOWN = 270
RIGHT =0
LEFT = 180



class Snake:
    def __init__(self):
        self.segment = []
        self.create_snake()
        self.head = self.segment[0]
    def create_snake(self):
        for block in INIT_POSI :        
            cube = Turtle("square")
            cube.color("white")
            cube.penup()
            cube.goto(block)
            self.segment.append(cube)
    def move(self):
        for seg in range(len(self.segment) - 1 ,  0, -1 ):
            nx = self.segment[seg - 1].xcor()
            ny = self.segment[seg - 1].ycor()
            self.segment[seg].goto(nx,ny)
        self.head.forward(MOVE_DIST)

    def up(self):
         if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != DOWN:
            self.head.setheading(DOWN)
    def left(self):
         if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading() != LEFT:

            self.head.setheading(RIGHT)
    
        
        



