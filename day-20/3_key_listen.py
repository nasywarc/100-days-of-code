import time
from turtle import Screen, Turtle

def w_key():
    # if head.setheading()
    pass

def a_key():
    pass

def s_key():
    pass

def d_key():
    pass

screen = Screen()
screen.tracer(0) # animate is off
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')
segment_list = []

starting_pos = [(0, 0), (-20, 0), (-40, 0)]

for position in starting_pos:
    new_segment = Turtle('square')
    new_segment.penup()
    new_segment.color('white')
    new_segment.goto(position)
    segment_list.append(new_segment)

head = segment_list[0]
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.5)
    screen.listen()
    screen.onkey(fun=..., key=('w'))
    screen.onkey(fun=..., key=('s'))
    screen.onkey(fun=..., key=('d'))
    screen.onkey(fun=..., key=('a'))
    for segment in segment_list:
        segment.forward(40)
    








screen.mainloop()