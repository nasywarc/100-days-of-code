import time
import random

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

food = Turtle('square')
food.penup()
food.color('white')

found_food_pos = False
while not found_food_pos:
    random_x = random.randint(0, 600)
    random_y = random.randint(0, 600)
    if random_x % 20 == 0 and random_x >= -300 and random_y >-300 and random_x <= 300 and random_y <=300 and random_y % 20 == 0:
        found_food_pos = True

food_pos = (float(random_x), float(random_y))
food.goto(food_pos)
food_head = False
        
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
        if segment != head:
            segment.goto(head.position())
            head.forward(20)
            
    if head.position() == food_pos:
        last_pos = segment_list[len(segment_list)-1]
        food.goto(last_pos.pos())
        segment_list.append(food)

print(head.pos)





screen.mainloop()