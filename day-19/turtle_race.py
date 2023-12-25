from turtle import Turtle, Screen

window = Screen()
window.setup(width=500, height=400)
user_choice = window.textinput(title='Who will win?', prompt='Enter a color( red/orange/yellow/green/blue/purple )')
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
y_index = [-125, -75, -25, 25, 75, 125]

for turtle_index in range(0, 6):
    tim = Turtle(shape='turtle')
    tim.penup()
    tim.color(colors[turtle_index])
    tim.goto(x=-230, y=y_index[turtle_index])

window.exitonclick()

