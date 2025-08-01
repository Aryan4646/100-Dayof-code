from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.goto(0,265)
        self.hideturtle()
        self.disp()
        self.refres()

    def disp(self):
        self.clear()
        t = self.write(f"Score: {self.score}",align = "center", font=("Arial", 24, "normal"))

    def refres(self):
        self.disp()
        self.score += 1

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over", align = "center" , font =("Arial", 24, "normal") )





