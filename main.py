from turtle import Turtle, Screen
from random import choice

timmy = Turtle()

timmy.shape("turtle")
timmy.color("medium purple")

# # Draw a square
# for action in range(4):
#     timmy.forward(100)
#     timmy.right(90)
#
# # Draw a dashed line
# for step in range(25):
#     timmy.pendown()
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)

# # Draw different shapes
# FULL_DEGREE = 360
# ini_turn = 3
colors = ["blue", "pale green", "dark orange", "powder blue", "indian red", "dark magenta", "dim gray"]
#
# for action in range(3,11):
#     degree = FULL_DEGREE/ini_turn
#     for turn in range(ini_turn):
#         timmy.forward(50)
#         timmy.right(degree)
#         timmy.forward(50)
#     ini_turn += 1
#     timmy.color(choice(colors))


# Generate a random walk
angle = [0, 90, 180, 270]
timmy.speed(0) #draw faster
pen_size = 15

for action in range(200):
    timmy.setheading(choice(angle))
    timmy.pensize(pen_size)
    timmy.color(choice(colors))
    timmy.forward(50)
    # timmy.right(choice(angle))
    pen_size += 0.1


screen = Screen()
screen.exitonclick()

