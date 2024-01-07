import time
from turtle import Screen, Turtle

screen = Screen()
screen.tracer(0)
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')
snake_length = []
x_index = [-20, -40, -60]

for square in range(0, 3):
    new_square = Turtle(shape='square')
    new_square.penup()
    new_square.color('white')
    new_square.goto(x=x_index[square], y=-10)
    snake_length.append(new_square)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.5)
    for square in snake_length:
        square.forward(40)
        if square.xcor() > 580 or square.xcor() < -580 or square.ycor() > 580 or square.ycor() < -580:
            game_is_on = False



screen.exitonclick()