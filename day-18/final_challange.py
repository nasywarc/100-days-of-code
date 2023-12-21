import turtle as t
import random

color_list = [(202, 164, 110), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

tim = t.Turtle()
tim.hideturtle()    
tim.penup()
tim.speed('fastest')
tim.goto(-250, -250)
t.colormode(255)
tim_y = -250

for times in range(100):
    if times % 10 == 0:
        tim_y += 50
        tim.setx(-250)
        tim.sety(tim_y)
    tim.pendown()
    tim.dot(20, random.choice(color_list))
    tim.penup()
    tim.forward(50)
    
t.mainloop()