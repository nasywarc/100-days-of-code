from tkinter import *

window = Tk()

window.title('Mile to KM Converter')
window.config(padx=15, pady=15)

user_entry = Entry(width=10)
user_entry.grid(column=1, row=0)

miles = Label(text='Miles')
miles.grid(column=2, row=0)
miles.config(padx=5)

is_equal = Label(text='is equal to')
is_equal.grid(column=0, row=1)

result = Label(text='0')
result.grid(column=1, row=1)

kilometer = Label(text='Km')
kilometer.grid(column=2, row=1)


def miles_to_km():
    float_user = float(user_entry.get())
    calculate = round(float_user * 1.60934)
    result.config(text=calculate)


calculate_button = Button(text='Calculate', command=miles_to_km)
calculate_button.grid(column=1, row=2)


window.mainloop()
