from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '@']

    password_list = []

    password_list += [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]

    shuffle(password_list)
    password = ''.join(password_list)
    password_input.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- FIND DATA ------------------------------- #
def find_data():
    try:
        with open('data.json', 'r') as file:
            # Reading old data
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title='Error', message='No Data file found.')
    else:
        website = website_input.get().strip()
        if website in data:
            messagebox.showinfo(title=website, message=f"\n\nEmail: {data[website]['user_info']}\nPassword: {data[website]['password']}")
        else:
            messagebox.showinfo(title='Oops', message=f'No details for the {website} exists.')


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_input.get().strip()
    user = user_input.get().strip()
    password = password_input.get().strip()

    new_date = {website: {
        'user_info': user,
        'password': password
    }}

    if website == '' or user == '' or password == '':
        messagebox.showinfo(title='Oops', message="Please don't let any fields empty!")
    else:
        confirm_info = messagebox.askokcancel(title=website, message=f'These are the details entered:\n\nEmail: {user} \nPassword: {password} \n\nIs it ok to save?')
        if confirm_info:
            try:
                with open('data.json', 'r') as file:
                    # Reading old data
                    data = json.load(file)
            except FileNotFoundError:
                # Create new JSON file
                with open('data.json', 'w') as file:
                    json.dump(new_date, file, indent=4)
            else:
                # Updating old data with new data
                data.update(new_date)
                with open('data.json', 'w') as file:
                    # Saving updated data
                    json.dump(data, file, indent=4)
            finally:
                clean_fields()


def clean_fields():
    website_input.delete(0, END)
    user_input.delete(0, END)
    password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager 🔒")
window.config(padx=40, pady=40)

# Add image to the background
canvas = Canvas(width=220, height=300)
image = PhotoImage(file="lock.png")
canvas.create_image(116, 130, image=image)
canvas.grid(row=0, column=1)


# Web site
website_label = Label(text='Website:')
website_label.grid(row=1, column=0)

website_input = Entry(width=21)
website_input.grid(row=1, column=1)
website_input.focus()

search_button = Button(text='Search', width=7, command=find_data)
search_button.grid(row=1, column=2)


# Email / username
user_label = Label(text='Email/Username:')
user_label.grid(row=2, column=0)

user_input = Entry(width=35)
user_input.grid(row=2, column=1, columnspan=2)
user_input.insert(0, 'user@mail.com')


# Password
password_label = Label(text='Password:')
password_label.grid(row=3, column=0)

password_input = Entry(width=20)
password_input.grid(row=3, column=1)

password_button = Button(text='Generate Password', command=password_generator, width=11)
password_button.grid(row=3, column=2)


# Add button
add_button = Button(text='Add', width=30, command=save)
add_button.grid(row=4, column=1, columnspan=2)


window.mainloop()
