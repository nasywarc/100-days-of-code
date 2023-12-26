from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')
x_index = [-50, -30, -10]

for square in range(0, 3):
    new_square = Turtle(shape='square')
    new_square.penup()
    new_square.color('white')
    new_square.goto(x=x_index[square], y=-10)    
    


screen.exitonclick()