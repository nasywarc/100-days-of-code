import tkinter
from tkinter import *

window = Tk()
window.title('My First GUI Program')
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)


# Label
my_label = tkinter.Label(text='I Am a Label', font=('Arial', 24, 'bold'))
my_label.grid(column=0, row=0)
my_label.config(padx=20, pady=20)

# setting the Label
my_label['text'] = 'New Text'
my_label.config(text='New Text')


# Button
def button_clicked():
    print('I got clicked')
    text = my_input.get()
    my_label.config(text=text)


my_button = Button(text='Click Me', command=button_clicked)
my_button.grid(column=1, row=1)
my_button.config(padx=20, pady=20)

my_button_2 = Button(text='Click Me 2', command=button_clicked)
my_button_2.grid(column=2, row=0)
my_button_2.config(padx=20, pady=20)

# Entry
my_input = Entry(width=10)
my_input.grid(column=3, row=2)


window.mainloop()
