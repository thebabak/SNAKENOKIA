#
from turtle import Turtle
UP =90
DOWN = 270
LEFT=180
RIGHT=0 

START_POS=[(-200,0),(-220,0),(-240,0)]
MOVE_DIS=20
class SnakeMod:
    def __init__(self):
        self.position_snake=[]
        self.create_snake()
        self.head=self.position_snake[0]
    def create_snake(self):
        for position in START_POS:
            self.add_segment(position)
    def add_segment(self,position):
        snake=Turtle("square")
        snake.color("white")
        snake.penup()
        snake.goto(position) 
        self.position_snake.append(snake)
    
    def reset(self):
        for s in self.position_snake:
            s.goto(1000,100)
        self.position_snake.clear()
        self.create_snake()
        self.head=self.position_snake[0]
        
        
        
    def extend(self):
        self.add_segment(self.position_snake[-1].position())
        
    
    def move(self):
        for mogh in range(len(self.position_snake)-1,0,-1):
            X=self.position_snake[mogh-1].xcor()
            Y=self.position_snake[mogh-1].ycor()

            self.position_snake[mogh].goto(X,Y)
        self.head.forward(MOVE_DIS)
    def up(self):
        if self.head.heading() !=DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() !=UP:
            self.head.setheading(DOWN)
    def left(self):
        if self.head.heading() !=RIGHT:
            
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading() !=LEFT:
    
            self.head.setheading(RIGHT)
            
    
