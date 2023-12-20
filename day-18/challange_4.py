import turtle as t
import random

tim = t.Turtle()
t.colormode(255)

########### Challenge 4 - Random Walk ########
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

tim.pensize(10)
tim.speed('fastest')

for times in range(200):
    direction = random.choice([1, 2, 3, 4])
    tim.color(random_color())
    tim.right(direction * 90)
    tim.forward(20)
    
t.mainloop()