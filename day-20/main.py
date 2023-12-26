from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')
snake_length = []
x_index = [-2, -1, 0]

for square in range(0, 3):
    new_square = Turtle(shape='square')
    new_square.color('white')
    new_square.goto(x=x_index[square], y=0)
    snake_length.append(new_square)
    
    


screen.exitonclick()