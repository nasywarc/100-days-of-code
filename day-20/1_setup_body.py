from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')

starting_pos = [(0, 0), (-20, 0), (-40, 0)]
for position in starting_pos:
    new_segment = Turtle('square')
    new_segment.color('white')
    new_segment.goto(position)









screen.mainloop()