from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position[0], position[1])

    def Up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(),y= new_y)
    def Down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(),y= new_y)



