from turtle import Turtle, Screen
import time
from SnakeMod import SnakeMod
from food import Food

from point import Score
screen=Screen()
screen.setup(width=600,height=600)

screen.bgcolor("black")
screen.title("snake nokia 3310")
screen.tracer(0)

MAR=SnakeMod()
FOODMOD=Food()
score=Score()

screen.listen()
screen.onkey(MAR.up,"Up")
screen.onkey(MAR.down,"Down")
screen.onkey(MAR.left,"Left")
screen.onkey(MAR.right,"Right")

        
game_on=True
while game_on:
    
    screen.update()
    
    time.sleep(.1)
    MAR.move()
    
    
    #eating food
    if MAR.head.distance(FOODMOD)<15:
        FOODMOD.refresh()
        MAR.extend()
        score.AddPoint()
    
    #wall
    if MAR.head.xcor()>280 or MAR.head.xcor() <-280 or MAR.head.ycor()>280 or MAR.head.ycor()<-280:
            score.reset()
            score.game_over()          

    for s in MAR.position_snake[1:]:
        if MAR.head.distance(s)<10:
            score.game_over() 
            score.reset()
        




screen.exitonclick()