import time
from turtle import Screen, Turtle

def move_forward():
    if head.heading() != 90:
        head.setheading(90)
    # head.forward(10)
    
def move_backward():
    if head.heading() != 270:
        head.setheading(270)
    # head.forward(10)
    
def move_right():
    if head.heading() != 0:
        head.setheading(0)
    # head.forward(10)
    
def move_left():
    # if head.heading() != 180:
    head.left(90)
    # head.forward(10)
    
    # head.setheading(180)
    # head.left(10)

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
    screen.onkey(fun=move_forward, key=('w'))
    screen.onkey(fun=move_backward, key=('s'))
    screen.onkey(fun=move_right, key=('d'))
    screen.onkey(fun=move_left, key=('a'))
    for segment in segment_list:
        segment.forward(40)
    








screen.mainloop()