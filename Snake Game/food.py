from turtle import Turtle
import random
from scoreboard import Scoreboard
class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        randX = random.randint(-280, 280)
        randY = random.randint(-280, 280)
        self.goto(randX, randY)
