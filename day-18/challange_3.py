import turtle as t

tim = t.Turtle()

########### Challenge 3 - Draw Shapes ########

for triangle in range(3):
    tim.forward(100)
    tim.right(120)
    
for square in range(4):
    tim.forward(100)
    tim.right(90)

for pentagon in range(5):
    tim.forward(100)
    tim.right(72)

for hexagon in range(6):
    tim.forward(100)
    tim.right(60)

for heptagon in range(7):
    tim.forward(100)
    tim.right(51.428)

for octagon in range(8):
    tim.forward(100)
    tim.right(45)

for nonagon in range(9):
    tim.forward(100)
    tim.right(40)

for decagon in range(10):
    tim.forward(100)
    tim.right(36)

t.mainloop()