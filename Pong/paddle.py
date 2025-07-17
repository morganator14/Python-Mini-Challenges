from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, x_coord, y_coord):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.goto(x_coord,y_coord)

    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
