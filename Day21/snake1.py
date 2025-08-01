from turtle import Turtle
START_POS = [(0,0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT= 0

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for i in START_POS:
            self.add_segment(i)

    def add_segment(self,position):
        segment = Turtle(shape="square")
        segment.color("white")
        segment.penup()
        segment.goto(position)
        self.segments.append(segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def snake_move(self):
        for seg_no in range(len(self.segments)-1,0,-1):
            new_x = self.segments[seg_no-1].xcor()
            new_y = self.segments[seg_no-1].ycor()
            self.segments[seg_no].goto(new_x,new_y)
        self.head.forward(MOVE_DISTANCE)

    def snake_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def snake_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def snake_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def snake_right(self):
        if self.head.heading != LEFT:
            self.head.setheading(RIGHT)