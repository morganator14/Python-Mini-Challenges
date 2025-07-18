from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segments(position)

    def add_segments(self, position):
        new_seg = Turtle("square")
        new_seg.color("white")
        new_seg.pu()
        new_seg.goto(position)
        self.segments.append(new_seg)

    def extend(self):
        self.add_segments(self.segments[-1].position())
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            newX = self.segments[seg_num - 1].xcor()
            newY = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(newX, newY)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
