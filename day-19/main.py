# Etch A Sketch
from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forwards():
    tim.forward(10)
    
def move_backwards():
    tim.back(10)
    
def clockwise():
    tim.right(10)
    
def c_clockwise():
    tim.left(10)
    
def reset_screen():
    tim.reset()
    
screen.listen()
screen.onkeypress(key='w', fun=move_forwards)
screen.onkeypress(key='a', fun=c_clockwise)
screen.onkeypress(key='s', fun=move_backwards)
screen.onkeypress(key='d', fun=clockwise)
screen.onkeypress(key='c', fun=reset_screen)


screen.exitonclick()