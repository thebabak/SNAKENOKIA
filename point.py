#point

from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        try:
            with open("data.txt") as data:
                self.high_score=int(data.read())
        except:
            self.high_score=0
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.hideturtle()
        self.Update_Point()
        
        
    def Update_Point(self):
        self.clear()
        self.write(f"Score: {self.score}   high score:{self.high_score}", align="center",font=("Arial",22,"normal"))
    
    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", align="center", font=FONT)

        
        self.goto(0, -100)
        self.write(f"Score: {self.score} ", align="center", font=FONT)
    
 

    def AddPoint(self):
        self.score +=1
        self.clear()
        self.Update_Point()
    def reset(self):
        if self.score>self.high_score:
           self.high_score= self.score
           with open("data.txt",mode="w") as data:
               data.write(f"{self.high_score}")
        self.score=0
        self.Update_Point()
        
   