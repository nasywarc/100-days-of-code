from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forward():
    if tim.heading() != 90:
        tim.setheading(90)
    tim.forward(10)
    
def move_backward():
    if tim.heading() != 270:
        tim.setheading(270)
    tim.forward(10)
    
def move_right():
    if tim.heading() != 0:
        tim.setheading(0)
    tim.forward(10)
    
def move_left():
    if tim.heading() != 180:
        tim.setheading(180)
    tim.forward(10)
    
    tim.setheading(180)
    tim.left(10)
    
def paint_toggle():
    if not tim.isdown():
        tim.pendown()
    else:
        tim.penup()
        
def reset_screen():
    tim.clear()
    tim.reset()
    tim.setheading(90)
    
tim.setheading(90)
screen.listen()
screen.onkey(fun=move_forward, key=('w'))
screen.onkey(fun=move_backward, key=('s'))
screen.onkey(fun=move_right, key=('d'))
screen.onkey(fun=move_left, key=('a'))
screen.onkey(fun=paint_toggle, key=('space'))
screen.onkey(fun=reset_screen, key=('r'))


screen.exitonclick()