from turtle import Turtle, Screen

window = Screen()
window.setup(width=500, height=400)
user_choice = window.textinput(title='Who will win?', prompt='Enter a color( red/orange/yellow/green/blue/purple )')
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

tim = Turtle(shape='turtle')
tim.penup()
tim.color('purple')
tim.goto(x=-230, y=125)
tom = Turtle(shape='turtle')
tom.color('blue')
tom.penup()
tom.goto(x=-230, y=75)
rim = Turtle(shape='turtle')
rim.color('green')
rim.penup()
rim.goto(x=-230, y=25)
rom = Turtle(shape='turtle')
rom.color('yellow')
rom.penup()
rom.goto(x=-230, y=-25)
gim = Turtle(shape='turtle')
gim.color('orange')
gim.penup()
gim.goto(x=-230, y=-75)
gom = Turtle(shape='turtle')
gom.color('red')
gom.penup()
gom.goto(x=-230, y=-125)

window.exitonclick()

