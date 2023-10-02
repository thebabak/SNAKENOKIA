from turtle import Turtle
import random as R

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=.5,stretch_wid=.5)
        self.color("White")
        self.speed("fastest")
        self.refresh()
        
    def  refresh(self):
        RAN_X=R.randint(-280,280)
        RAN_Y=R.randint(-280,280)
        self.goto(RAN_X,RAN_Y)
        
        

        