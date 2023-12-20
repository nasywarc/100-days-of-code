import turtle as t
import random

tim = t.Turtle()

########### Challenge 4 - Random Walk ########
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

tim.pensize(10)
tim.speed('fastest')

for times in range(200):
    direction = random.choice([1, 2, 3, 4])
    tim.color(random.choice(colours))
    tim.right(direction * 90)
    tim.forward(20)
    
t.mainloop()