import turtle as t

tim = t.Turtle()

########### Challenge 2 - Draw a Dashed Line ########

for times in range(15):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()
    
t.mainloop()