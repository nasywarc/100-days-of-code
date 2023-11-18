from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password Manager')
window.config(padx=20, pady=20)

canvas = Canvas(width=220, height=220, highlightthickness=0)
logo = PhotoImage(file='logo.png')
canvas.create_image(110, 110, image=logo)
canvas.pack()


window.mainloop()
