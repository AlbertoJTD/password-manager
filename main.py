from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager 🔒")
window.config(padx=40, pady=40)

# Add image to the background
canvas = Canvas(width=220, height=300)
image = PhotoImage(file="lock.png")
canvas.create_image(112, 130, image=image)
canvas.grid(row=0, column=1)


# Web site
website_label = Label(text='Website:')
website_label.grid(row=1, column=0)

website_input = Entry(width=35)
website_input.grid(row=1, column=1, columnspan=2)


# Email / username
user_label = Label(text='Email/Username:')
user_label.grid(row=2, column=0)

user_input = Entry(width=35)
user_input.grid(row=2, column=1, columnspan=2)


# Password
password_label = Label(text='Password: ')
password_label.grid(row=3, column=0)

password_input = Entry(width=35)
password_input.grid(row=3, column=1, columnspan=2)

password_button = Button(text='Generate Password')
password_button.grid(row=3, column=2)


# Add button
add_button = Button(text='Add', width=30)
add_button.grid(row=4, column=1, columnspan=2)


window.mainloop()
