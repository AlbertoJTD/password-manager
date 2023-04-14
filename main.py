from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager 🔒")
window.config(padx=20, pady=20)

# Add image to the background
canvas = Canvas(width=512, height=512)
image = PhotoImage(file="lock.png")
canvas.create_image(256, 150, image=image)
canvas.pack()

window.mainloop()
