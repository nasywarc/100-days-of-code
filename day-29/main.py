from random import choice, randint, shuffle
from tkinter import *
from tkinter import messagebox
import pyperclip

file_path = 'data.txt'
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
               'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():

    if len(website_entry.get()) == 0 or len(password_entry.get()) == 0:
        messagebox.showwarning(
            title='Oops', message='Please don\'t leave any fields empty!')
    else:

        is_ok = messagebox.askokcancel(title=website_entry.get(
        ), message=f'These are the details entered:\nEmail:{email_usn_entry.get()}\nPassword: {password_entry.get()}\nIs it okay to save?')

        if is_ok:
            with open(file_path, "a", newline='', encoding="cp437", errors='ignore') as pass_file:
                pass_file.write(
                    f'\n{website_entry.get()}\t\t{email_usn_entry.get()}\t\t{password_entry.get()}')

        # deleting entry after button get pressed
        website_entry.delete(0, END)
        password_entry.delete(0, END)

        website_entry.focus()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)

# Canvas
canvas = Canvas(width=200, height=200, highlightthickness=0)
logo = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

# Label
website_label = Label(text='Website:')
website_label.grid(row=1, column=0)
email_usn_label = Label(text='Email/Username:')
email_usn_label.grid(row=2, column=0)
password_label = Label(text='Password:')
password_label.grid(row=3, column=0)

# Entry
website_entry = Entry()
website_entry.grid(row=1, column=1, columnspan=2, sticky="EW")
website_entry.focus()  # autofocusing the cursor
email_usn_entry = Entry()
email_usn_entry.grid(row=2, column=1, columnspan=2, sticky="EW")
email_usn_entry.insert(0, 'dummy@gmail.com')
password_entry = Entry()
password_entry.grid(row=3, column=1, sticky="EW")

# Button
generate_button = Button(text='Generate Password', command=generate_password)
generate_button.grid(row=3, column=2, sticky="EW")
add_button = Button(text='Add', command=save)
add_button.grid(row=4, column=1, columnspan=2, sticky="EW")

window.mainloop()
