from tkinter import *
import os

file_path = 'data.txt'
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_password():
    if os.path.exists(file_path):
        with open(file_path, "a", newline='', encoding="cp437", errors='ignore') as pass_file:
            pass_file.write(
                f'\n{website_entry.get()}\t\t{email_usn_entry.get()}\t\t{password_entry.get()}')
    else:
        with open(file_path, "x", newline='', encoding="cp437", errors='ignore') as pass_file:
            pass_file.write(
                f'{website_entry.get()}\t\t{email_usn_entry.get()}\t\t{password_entry.get()}')


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

website_label = Label(text='Website:')
website_label.grid(row=1, column=0)

email_usn_label = Label(text='Email/Username:')
email_usn_label.grid(row=2, column=0)

password_label = Label(text='Password:')
password_label.grid(row=3, column=0)

website_entry = Entry()
website_entry.grid(row=1, column=1, columnspan=2, sticky="EW")
website_entry.focus()  # auto focusing the cursor

email_usn_entry = Entry()
email_usn_entry.grid(row=2, column=1, columnspan=2, sticky="EW")
email_usn_entry.insert(0, 'dummy@gmail.com')

password_entry = Entry()
password_entry.grid(row=3, column=1, sticky="EW")

generate_button = Button(text='Generate Password')
generate_button.grid(row=3, column=2, sticky="EW")

add_button = Button(text='Add', command=save_password)
add_button.grid(row=4, column=1, columnspan=2, sticky="EW")

window.mainloop()
