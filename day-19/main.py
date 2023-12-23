from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(10)
    
def move_backward():
    tim.setheading(270)
    tim.forward(10)
    
def move_right():
    tim.setheading(0)
    tim.right(10)
    
def move_left():
    tim.setheading(180)
    tim.left(10)
    
tim.setheading(90)
screen.listen()
screen.onkey(fun=move_forward, key=('w'))
screen.onkey(fun=move_backward, key=('s'))
screen.onkey(fun=move_right, key=('d'))
screen.onkey(fun=move_left, key=('a'))
screen.exitonclick()