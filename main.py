import turtle as t
from turtle import Turtle, Screen, speed, pensize, resizemode, width
import random

tim = t.Turtle()
t.colormode(255)
my_screen = Screen()
tim.pensize(10)
tim.speed(10)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color= (r, g, b)
    return random_color


direction = [0, 90, 180, 270]


#def random_walk():
    # tim.forward(20)
    # random.choice(direction)


for _ in range(0, 500):
    direct_pick = random.choice(direction)
    tim.color(random_color())
    tim.forward(20)
    tim.setheading(direct_pick)


my_screen.exitonclick()
