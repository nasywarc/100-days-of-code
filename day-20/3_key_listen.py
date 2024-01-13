import time
from turtle import Screen, Turtle

def w_key():
    if head.heading() == 0 or head.heading() == 180:
        head.setheading(90)

def a_key():
    if head.heading() == 90 or head.heading() == 270:
        head.setheading(180)

def s_key():
    if head.heading() == 0 or head.heading() == 180:
        head.setheading(270)

def d_key():
    if head.heading() == 90 or head.heading() == 270:
        head.setheading(0)

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
    time.sleep(0.4)
    screen.listen()
    screen.onkey(fun=w_key, key=('w'))
    screen.onkey(fun=a_key, key=('a'))
    screen.onkey(fun=s_key, key=('s'))
    screen.onkey(fun=d_key, key=('d'))
    for segment in segment_list:
        segment.forward(40)
    








screen.mainloop()