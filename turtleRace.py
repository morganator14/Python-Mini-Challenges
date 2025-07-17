from turtle import Turtle, Screen
import random


screen = Screen()
screen.setup(width=500,height=400)
user_bet = screen.textinput(title = "make your bet", prompt = " Which turtle will win? Enter a color:")
colors = ["red","orange","yellow","green","blue","purple"]
all_turtles = []

race_on = False
y_val = -110
for c in colors:
    new_turt = Turtle(shape = "turtle")
    new_turt.color(c)
    new_turt.pu()
    y_val += 35
    new_turt.goto(-230, y_val)
    all_turtles.append(new_turt)

if user_bet:
    race_on = True
while race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle was the fastest!")
            else:
                print(f"Darn. The {user_bet} turtle was not quick enough, you lose.")
            race_on = False
        rand_dist = random.randint(0,10)
        turtle.forward(rand_dist)
screen.exitonclick()