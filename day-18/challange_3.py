import turtle as t
import random as r

tim = t.Turtle()

########### Challenge 3 - Draw Shapes ########

def shape(side):
    tim.color(r.choice(color_list))
    angle = 360/side
    for allshape in range(side):
        tim.forward(100)
        tim.right(angle)

color_list = ['cyan', 'bisque3', 'coral', 'darkgreen', 'lightcoral']

for number in range(3, 11):
    shape(number)

t.mainloop()